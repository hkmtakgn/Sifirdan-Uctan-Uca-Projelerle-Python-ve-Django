from django.shortcuts import redirect, render
from my_weblog.forms import PostForm
from django.contrib import messages
from my_weblog.models import PostModel
# Create your views here.


def home_views(request):
  posts = PostModel.objects.filter(is_active=True)
  context = dict(posts=posts, )
  return render(request, "pages/home.html", context)


def add_post(request):
  post_form = PostForm()
  if request.method == "POST":
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      post_form.save()
      messages.success(request, "Post kaydedildi !")
      return redirect("add_post")
    else:
      post_form = PostForm()
      messages.warning(request, "Bilgiler eksik veya hatalı !")
      return redirect("add_post")
  context = dict(post_form=post_form, )
  return render(request, "pages/add-post.html", context)
