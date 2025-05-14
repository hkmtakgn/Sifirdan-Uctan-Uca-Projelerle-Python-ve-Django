from django.shortcuts import render,get_object_or_404
from XDEVS.models import User,Category,Tag

# Create your views here.



def dev_views (request,cat_slug=None,tag_slug=None,id=None):
    if not cat_slug and not tag_slug and not id:
        info = "categories"
        title = "Categeories"
        items = Category.objects.filter (is_active=True)
    elif cat_slug and not tag_slug and not id:
        info = "tags"
        title = "Category Details"
        category = get_object_or_404 (Category,slug=cat_slug)
        items = Tag.objects.filter (category=category)
    elif cat_slug and tag_slug and not id :
        info = "xdevs"
        title = "X-Developers"
        category = get_object_or_404 (Category,slug=cat_slug)
        tag = get_object_or_404 (Tag,category=category,slug=tag_slug)
        items = tag.user_set.filter (is_active=True)
    elif cat_slug and tag_slug and id :
        info = "devinfo"
        title = "X-Developer Details"
        items = User.objects.filter (tag__slug=tag_slug,tag__category__slug=cat_slug,pk=id)
    context = dict (
        items=items,
        page_title=title,
        info=info,
    )
    return render (request,"main/home.html",context)

