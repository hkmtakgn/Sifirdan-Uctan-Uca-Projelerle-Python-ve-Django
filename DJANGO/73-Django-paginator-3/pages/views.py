from django.shortcuts import render,get_object_or_404,redirect
from pages.models import Page,Developer
from django.core.paginator import Paginator

# Create your views here.


def page_views (request,page_slug=None):
    developers = Developer.objects.filter (is_active=True)

    devs = Paginator (developers,3)
    page_number = request.GET.get ("page")
    items = devs.get_page (page_number)

    if not page_slug and request.path == "/":
        return redirect('ana-sayfa/')
    elif page_slug:
        page = get_object_or_404 (Page,slug=page_slug)
    context = dict (
        page=page,
        items=items,
    )
    return render (request,"page/page_views.html",context)

