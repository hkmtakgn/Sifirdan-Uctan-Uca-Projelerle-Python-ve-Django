from django.shortcuts import render
from django.http import Http404

# Create your views here.

def page_views (request,slug=None):
    if not slug:
        slug = "home"
        title = "Home Page"
        context = dict (
        page_title=title,
        slug=slug,
        )
        return render (request,"page/page_views.html",context)
    elif slug == "vision":
        title = "Vision Page"
        slug = "vision"
        context = dict (
            page_title=title,
            slug=slug,
        )
        return render (request,"page/page_views.html",context)
    elif slug == "contact":
        slug = "contact"
        title = "Contact Page"
        context = dict (
            page_title=title,
            slug=slug,
        )
        return render (request,"page/page_views.html",context)
    raise Http404 ("Sayfa bulunamadı...")
