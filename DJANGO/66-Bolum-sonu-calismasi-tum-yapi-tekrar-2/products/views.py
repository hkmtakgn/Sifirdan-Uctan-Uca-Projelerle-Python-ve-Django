from django.shortcuts import render
from django.http import Http404

# Create your views here.

def pro_views (request,pro_slug=None):
    if not pro_slug:
        title = 'Products Page'
        context = dict (
        page_title=title,
        )
        return render (request,'products/products.html',context)
    elif pro_slug == 'web-development':
        title = 'Web Development'
        context = dict (
            page_title=title,
        )
        return render (request,'products/web_development.html',context)
    else:
        return Http404 ()

