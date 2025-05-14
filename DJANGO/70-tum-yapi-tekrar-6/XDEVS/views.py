from django.shortcuts import render,get_object_or_404
from XDEVS.models import Category,Developer,Tag
from django.http import Http404

# Create your views here.



def main_views (request):
    title = 'Home Page'
    context = dict (
        page_title=title,
    )
    return render (request,'main/main.html',context)

def x_views (request,cat_slug=None,id=None,tag_slug=None):
    if not cat_slug and not id and not tag_slug:
        title = 'Categories'
        items = Category.objects.filter (is_active=True)
        context = dict (
        page_title=title,
        items=items,
    )
        return render (request,'main/x_categories.html',context)
    elif cat_slug and not id and not tag_slug:
        title = cat_slug.title
        category = get_object_or_404 (Category,slug=cat_slug)
        items = category.developer.all ()
        context = dict (
            page_title=title,
            items=items,
        )
        return render (request,'main/category_details.html',context)
    elif id and not tag_slug:
        title = 'X-Developer Details'
        context = dict (
            page_title=title,
            item=get_object_or_404(Developer,pk=id),
        )
        return render (request,'main/x_details.html',context)
    elif tag_slug:
        title = 'Tag Details'
        tag = get_object_or_404 (Tag,slug=tag_slug,is_active=True)
        items = tag.developer_set.all()
        context = dict (
            page_title=title,
            items=items,
        )
        return render (request,'main/category_details.html',context)
    else:
        raise Http404('Sayfa bulunamadi!')
