from django.shortcuts import redirect, render

from weblog.forms.forms import PostForm
from weblog.models import Blog_Post
# Create your views here.


def home_views(request):
  items = Blog_Post.objects.filter(is_active=True)
  post_form = PostForm()
  context = dict(
      post_form=post_form,
      items=items,
  )
  return render(request, "pages/home.html", context)


def add_post(request):
  if request.method == "POST":
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      post_form.save()
      return redirect("blog_home")
    else:
      post_form = PostForm()
      return redirect("blog_home")
  else:
    post_form = PostForm()
  context = dict(post_form=post_form, )
  return render(request, "pages/home.html", context)
