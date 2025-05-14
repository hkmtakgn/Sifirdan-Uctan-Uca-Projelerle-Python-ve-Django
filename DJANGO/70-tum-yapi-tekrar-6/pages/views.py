from django.shortcuts import render
from pages.models import Category,Tag,Developer
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.

@login_required(login_url="/admin/login/")
def home_views (request):
    title = "X-Developers"
    devs = Developer.objects.filter (is_active=True)
    items = Category.objects.filter (is_active=True)
    context = dict (
        page_title=title,
        categories=items,
        devs=devs,
    )
    return render (request,"main/home.html",context)

@login_required(login_url="/admin/login/")
def cat_views (request,cat_slug):
    category = get_object_or_404 (Category,slug=cat_slug)
    tags = category.tag_set.filter (is_active=True)
    title = category.title.capitalize() + " Details"
    context = dict (
        page_title=title,
        tags=tags,
    )
    return render (request,"main/cat_details.html",context)

@login_required(login_url="/admin/login/")
def tag_views (request,cat_slug,tag_slug):
    category = get_object_or_404 (Category,slug=cat_slug)
    tag = get_object_or_404 (Tag,slug=tag_slug,category=category)
    title = tag.title + " Details"
    context = dict (
        page_title=title,
        tags=tag.developer_set.all,
    )
    return render (request,"main/tag_details.html",context)

@login_required(login_url="/admin/login/")
def dev_views (request,id):
    dev = get_object_or_404 (Developer,pk=id)
    title = "X-Developer Details"
    context = dict (
        page_title=title,
        item=dev,
    )
    return render (request,"main/dev_details.html",context)


def logout_views (request):
    logout(request)
    return redirect ("/")

