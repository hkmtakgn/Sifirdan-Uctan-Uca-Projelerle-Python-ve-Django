from django.contrib import messages
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from weblog.forms import PostForm
from weblog.models import Post

# Create your views here.
from weblog.models import Tag
import json
from django.contrib.messages import Message


def home_views(request):
  posts = Post.objects.filter(is_active=True)
  title = "Home Page"
  context = dict(
      page_title=title,
      posts=posts,
  )
  return render(request, "pages/home.html", context)


def add_post_views(request):
  if request.method == "POST":
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      tags = json.loads(post_form.cleaned_data.get("add_tag"))
      post = post_form.save(commit=False)
      tag_objects = []
      for item in tags:
        tag1, created = Tag.objects.get_or_create(title=item["value"])
        tag_objects.append(tag1)
        post.save()
        post.tag.set(tag_objects)
        post_form.save()
        messages.info(request, "The post has been successfully saved!")
      return redirect("home")
  else:
    post_form = PostForm()
  title = "Add Post Page"
  context = dict(
      page_title=title,
      post_form=post_form,
  )
  return render(request, "pages/add-post.html", context)


def delete_item(request, id):
  post = get_object_or_404(Post, id=id, is_active=True)
  post.delete()
  return redirect("home")


def edit_item(request, id):
  post = get_object_or_404(Post, id=id, is_active=True)
  if request.method == "POST":
    post_form = PostForm(request.POST, instance=post)
    if post_form.is_valid():
      post_form.save()
      return redirect("home")
  else:
    post_form = PostForm(instance=post)
  context = dict(post_form=post_form, )
  return render(request, "pages/add-post.html", context)


def favorites_views(request):
  favs = Post.objects.filter(favs=True)
  context = dict(favs=favs)
  return render(request, "pages/favorites.html", context)


def add_favs(request, id):
  post = get_object_or_404(Post, id=id, is_active=True)
  if not post.favs:
    post.favs = True
    post.save()
    return redirect("favorites")
  else:
    post.favs = False
    post.save()
    return redirect("favorites")
