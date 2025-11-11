from django.shortcuts import render, redirect
from blog.models import post_model
from blog.forms.post_form import PostForm

# Create your views here.


def blog_home_views(request):
  posts = post_model.objects.all()
  context = dict(posts=posts, )
  return render(request, "blog/blog_home.html", context)


def add_post_views(request):
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("blog_home")
  else:
    form = PostForm()
    context = dict(form=form, )
    return render(request, "blog/add_post.html", context)
