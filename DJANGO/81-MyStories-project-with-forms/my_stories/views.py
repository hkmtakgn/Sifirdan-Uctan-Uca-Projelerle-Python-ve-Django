from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from my_stories.forms.post_form import PostForm
from my_stories.models import post_model

# Create your views here.


def posts_home_views(request):
  posts = post_model.objects.all()
  if request.method == "POST":
    users = User.objects.all()
    form_user = request.POST.get("username")
    form_password = request.POST.get("password")
    user = authenticate(username=form_user, password=form_password)
    if user is None:
      messages.warning(request, "User not found")
      return redirect("posts_home")
    else:
      login(request, user)
      messages.info(request, "User authenticated")
      return redirect("posts_home")
  else:
    context = dict(posts=posts, )
    return render(request, "posts/posts_home.html", context)


def logout_views(request):
  logout(request)
  messages.success(request, "User logged out")
  return redirect("posts_home")


def login_views(request):
  return redirect("posts_home")


def post_add(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Post created")
      return redirect("posts_home")
    else:
      messages.warning(request, "Invalid form")
      return redirect("posts_home")
  else:
    form = PostForm()
    context = dict(form=form, )
    return render(request, "posts/add_post_form.html", context)
