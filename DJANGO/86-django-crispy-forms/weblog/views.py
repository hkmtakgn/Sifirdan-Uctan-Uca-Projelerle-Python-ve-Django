from django.shortcuts import render
# Create your views here.

from weblog.forms.forms import PostForm


def home_views(request):
  post_form = PostForm()
  context = dict(post_form=post_form, )
  return render(request, "pages/home.html", context)
