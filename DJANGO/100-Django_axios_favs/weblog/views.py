from django.shortcuts import redirect, render, get_object_or_404
from weblog.models import FavPost, Interface_user, Page
from weblog.forms import PageForm, PostForm, UserForm
from django.contrib import messages
from weblog.models import Post

# Create your views here.


def general_views(request, page_slug=None):
    if page_slug:
        page = get_object_or_404(Page, page_slug=page_slug, is_active=True)
        if page_slug == "post-share":
            return post_share(request)
        elif page_slug == "add-page":
            return add_page(request)
        elif page_slug == "register":
            return register(request)
        elif page_slug == "contact":
            return contact(request)
        elif page_slug == "favorites":
            return favorites(request)
        else:
            if page_slug == page.page_slug:
                title = page.title
                context = dict(
                    page_slug=page_slug,
                    page_title=title,
                    page=page,
                )
                return render(request, "pages/page-detail.html", context)
    if not page_slug:
        title = "Home"
        context = dict(page_title=title, )
        return render(request, "pages/home.html", context)


def post_share(request):
    title = "Add Post"
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.info(request, "Post is saved!")
            return redirect("/")
    else:
        post_form = PostForm()
        context = dict(
            post_form=post_form,
            page_title=title,
        )
        return render(request, "pages/share-post.html", context)


def add_page(request):
    title = "Add Page"
    if request.method == "POST":
        page_form = PageForm(request.POST, request.FILES)
        if page_form.is_valid():
            page_form.save()
            return redirect("/")
    else:
        page_form = PageForm()

    context = dict(
        page_form=page_form,
        page_title=title,
    )
    return render(request, "pages/add-page.html", context)


def register(request):
    title = "Register"
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            Interface_user.objects.update(is_online=False)
            user_form.save()
            return redirect("/")
    else:
        user_form = UserForm()

    context = dict(
        user_form=user_form,
        page_title=title,
    )
    return render(request, "pages/register-user.html", context)


def contact(request):
    title = "Contact"
    context = dict(page_title=title, )
    return render(request, "pages/contact.html", context)


def global_posts(request):
    g_posts = Post.objects.filter(is_active=True, user__is_online=True)
    return dict(g_posts=g_posts, )


def post_detail_views(request, id):
    post = get_object_or_404(Post, id=id, is_active=True)
    context = dict(post=post, )
    return render(request, "pages/post-detail.html", context)


def login_views(request):
    title = "Login"
    if request.method == "POST":
        form_email = request.POST.get('email')
        form_password = request.POST.get('password')
        for user in Interface_user.objects.all():
            if user.email == form_email and user.password == form_password:
                Interface_user.objects.update(is_online=False)
                log_user = get_object_or_404(Interface_user,
                                             email=form_email,
                                             password=form_password)
                log_user.is_online = True
                log_user.save()
                messages.info(request, f"Welcome {log_user.first_name}!")
                return redirect('weblog:home')
    else:
        pass
    context = dict(page_title=title, )
    return render(request, "pages/login.html", context)


def fav_update_views(request):
    if request.method == "POST":
        user = get_object_or_404(Interface_user, is_online=True)
        fav_post = get_object_or_404(Post,
                                     is_active=True,
                                     slug=request.POST.get("slug"),
                                     user=user)
        fav_set, created = FavPost.objects.get_or_create(user=user,
                                                         post=fav_post)
        if not created:
            fav_set.is_active = not fav_set.is_active
            fav_set.save()
            return redirect("weblog:home")


def favorites(request):
    title = "Favorites"
    user = get_object_or_404(Interface_user, is_online=True)
    fav_posts = FavPost.objects.filter(is_active=True, user=user)
    context = dict(
        page_title=title,
        fav_posts=fav_posts,
    )
    return render(request, "pages/favorites.html", context)
