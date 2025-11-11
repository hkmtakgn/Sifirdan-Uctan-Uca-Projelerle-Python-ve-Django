from django.shortcuts import redirect, render
from weblog.models import Post
from weblog.forms import PostForm
# Create your views here.


def weblog_home(request):
  posts = Post.objects.filter(is_active=True)
  context = dict(posts=posts, )
  return render(request, "pages/weblog_home.html", context)


def add_post(request):
  post_form = PostForm()
  if request.method == "POST":
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      post_form.save()
      return redirect("home")
  context = dict(post_form=post_form, )
  return render(request, "pages/add_post.html", context)
