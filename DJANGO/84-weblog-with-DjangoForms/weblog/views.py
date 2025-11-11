from django.shortcuts import render
from weblog.forms.forms import BlogForm
# Create your views here.


def home_views(request):
  post_form = BlogForm()
  context = dict(post_form=post_form, )
  return render(request, "blog/home.html", context)
