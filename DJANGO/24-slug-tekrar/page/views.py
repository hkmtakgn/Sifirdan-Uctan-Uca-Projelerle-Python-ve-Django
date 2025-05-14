from django.shortcuts import render
from .fake_db.pages import fake_db_project
from django.http import Http404

# Create your views here.


def viewer (request,slug=None):
    if not slug:
        title = fake_db_project[0]["url"]
        detail = fake_db_project[0]["detail"]
        slug = "slug"
        context = dict (
            page_title=title,
            page_detail=detail,
            slug=slug,
        )
        
        return render (request,"page/views.html",context)
    
    result = list(filter(lambda x: (x["url"] == slug),fake_db_project))
    if result:
        title=result[0]["url"]
        detail=result[0]["detail"]
        context = dict (
            page_title=title,
            page_detail=detail,
        )
        return render (request,"page/views.html",context)
    
    raise Http404("Sayfa bulunamadı...")
