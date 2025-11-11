from django.shortcuts import render, get_object_or_404, redirect
from fotoblog.models import Page, Post, FavPost
from fotoblog.forms.forms import PageForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.paginator import Paginator


def page_views(request,
               page_slug=None,
               post_slug=None,
               post_detail_slug=None,
               post_id=None):
    if post_id:
        return post_detail_views(request, post_id)
    if post_slug:
        return post_share(request, post_slug)
    if page_slug == "login":
        return login_views(request)
    if page_slug == "logout":
        return logout_views(request)
    if page_slug == "register":
        return register(request)
    if page_slug == "post-share":
        return post_share(request)
    if page_slug == "fav-update":
        return fav_update(request)
    if page_slug == "favorites":
        return favorites_views(request, page_slug)
    if page_slug == "page-details":
        return post_detail_views(request, page_slug, post_slug)
    if page_slug and not page_slug == "home":
        page = get_object_or_404(Page, slug=page_slug, is_active=True)
        if page_slug == "add-page":
            if request.user.is_authenticated and request.user.is_superuser:
                return add_page(request, page_slug)
            else:
                return redirect("fotoblog:home_views")
    elif page_slug == None or page_slug == "home":
        p_posts = Post.objects.filter(is_active=True).order_by("-id")
        set_posts = Paginator(p_posts, 3)
        page_number = request.GET.get("page")
        posts = set_posts.get_page(page_number)
        title = "Home"
        page = get_object_or_404(Page, slug="home", is_active=True)
        context = dict(
            posts=posts,
            page=page,
        )
        return render(request, "fb_pages/page-views.html", context)
    context = dict(page=page, )
    return render(request, "fb_pages/page-views.html", context)


def add_page(request, page_slug):
    if request.method == "POST":
        page_form = PageForm(request.POST, request.FILES)
        if page_form.is_valid():
            form_title = request.POST.get("title")
            is_page = Page.objects.filter(title__icontains=form_title).exists()
            if not is_page:
                page_form.save()
                messages.success(request,
                                 "The page has been successfully added!")
            else:
                messages.warning(request, "Already exists!")
            return redirect("fotoblog:home_views")
    else:
        page_form = PageForm()
    context = dict(page_form=page_form,
                   page=get_object_or_404(Page, slug=page_slug))
    return render(request, "fb_pages/page-views.html", context)


def login_views(request):
    title = "Login"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        login_user = authenticate(username=username, password=password)
        if login_user is not None:
            auth_login(request, login_user)
            messages.info(request, "Logged in successfuly!")
            return redirect("fotoblog:home_views")
        else:
            messages.warning(request, "Invalid username or password!")
    context = dict(page_title=title, )
    return render(request, "fb_pages/login-page.html", context)


def logout_views(request):
    logout(request)
    messages.success(request, "Logged out successfuly!")
    return redirect("fotoblog:home_views")


def register(request):
    title = "Register"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            register_user = authenticate(username=username, password=password)
            if register_user is not None:
                auth_login(request, register_user)
                messages.warning(request, "User is already exists!")
                return redirect("fotoblog:home_views")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request,
                                 "The user has been successfully registered!")
                return redirect("fotoblog:home_views")

    context = dict(page_title=title, )
    return render(request, "fb_pages/register-page.html", context)


def post_share(request, post_slug=None):
    post = None
    if post_slug:
        post = get_object_or_404(Post, slug=post_slug, is_active=True)
    if request.method == "POST":
        if post:
            post_form = PostForm(request.POST, request.FILES, instance=post)
        else:
            post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_obj = post_form.save(commit=False)
            title = post_form.cleaned_data.get("title")
            slug = slugify(title)

            if not post:
                if Post.objects.filter(slug=slug).exists():
                    messages.warning(request, "Post already exists!")
                    return render(request, "fb_pages/post-share.html",
                                  {"post_form": post_form})
            else:
                if Post.objects.filter(slug=slug).exclude(id=post.id).exists():
                    messages.warning(
                        request,
                        "Another post with this title already exists!")
                    return render(request, "fb_pages/post-share.html",
                                  {"post_form": post_form})

            post_obj.slug = slug
            post_obj.save()
            if post:
                messages.success(request, "Post updated successfully!")
            else:
                messages.success(request, "Post saved successfully!")
            return redirect("fotoblog:home_views")
    else:
        post_form = PostForm(instance=post)

    return render(request, "fb_pages/post-share.html", {"post_form": post_form})


def fav_update(request):
    if request.method == "POST":
        fav_post = get_object_or_404(Post, slug=request.POST.get("buttonSlug"))
        favset, created = FavPost.objects.get_or_create(user=request.user,
                                                        post=fav_post)
        if not created:
            favset.is_selected = not favset.is_selected
            favset.save()
        else:
            favset.is_selected = True
            favset.save()
            messages.success(request, "Post saved to Favorites!")
        return redirect("fotoblog:home_views")


def favorites_views(request, page_slug):
    title = "Favorites"
    user = request.user
    page = get_object_or_404(Page, slug=page_slug, is_active=True)
    fav_posts = FavPost.objects.filter(is_selected=True, user=user)
    context = dict(page_title=title, fav_posts=fav_posts, page=page)
    return render(request, "fb_pages/page-views.html", context)


def post_detail_views(request, page_slug, post_slug, post_id):
    title = "Post Details"
    post = get_object_or_404(Post, id=post_id, slug=post_slug, is_active=True)
    page = get_object_or_404(Page, slug=page_slug)
    context = dict(
        page_title=title,
        post=post,
        page=page,
    )
    return render(request, "fb_pages/page-views.html", context)
