from django.shortcuts import render
from django.http import Http404
from global_processor.global_db import global_pages

# Create your views here.

def home (request,path):
    pages = global_pages(request).get('pages', [])
    vision_page = next((page for page in pages if page['url'] == 'vision'), None)
    if path == "/":
        title = "Ana Sayfa"
        context = dict (
            page_title=title,
        )
    elif path == "vision":
        title = "Vizyonumuz"
        context = dict (
            page_title=title,
            vision_details=vision_page['details'],
        )
    elif path == "contact":
        title = "İletişim"
        context = dict (
            page_title=title,
        )
    else:
        raise Http404
    return render (request,"pages/home.html",context)

