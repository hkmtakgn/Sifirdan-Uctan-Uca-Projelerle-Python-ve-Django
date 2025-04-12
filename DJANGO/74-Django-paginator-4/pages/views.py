from django.shortcuts import render,get_object_or_404,redirect
from pages.models import Page,Developer
from django.core.paginator import Paginator

# Create your views here.


def page_views (request,page_slug=None):
    if not page_slug and request.path == "/":

        items = None

        return redirect('ana-sayfa/')
    elif page_slug:
        developers = Developer.objects.filter (is_active=True).order_by("id")

        devs = Paginator (developers,6)
        page_number = request.GET.get ("page")
        items = devs.get_page (page_number)

        page = get_object_or_404 (Page,slug=page_slug)

    context = dict (
        page=page,
        items=items,
    )
    return render (request,"page/page_views.html",context)

