from django.shortcuts import redirect, render
from weblog.models import Post
from weblog.forms import PostForm
from django.shortcuts import get_object_or_404


def home_views(request):
    posts = Post.objects.filter(is_active=True)
    title = "Home Page"
    context = dict(
        page_title=title,
        posts=posts,
    )
    return render(request, "pages/home.html", context)


def add_post_view(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
    else:
        post_form = PostForm()
    title = "Add Post"
    context = dict(
        page_title=title,
        post_form=post_form,
    )
    return render(request, "pages/add-post.html", context)


def delete_post_view(request, id):
    post = get_object_or_404(Post, pk=id, is_active=True)
    post.delete()
    return redirect("home")


def edit_post_view(request, id):
    post = get_object_or_404(Post, id=id, is_active=True)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm(instance=post)
        title = "Add Post"
        context = dict(
            page_title=title,
            post_form=post_form,
        )
        return render(request, "pages/add-post.html", context)
