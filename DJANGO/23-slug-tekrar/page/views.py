from django.shortcuts import render
from .fake_db.pages import FAKE_DB_PROJECTS
from django.http import Http404

# Create your views here.

def home (request):
    is_home = True,
    context = dict (
        is_home=is_home,
    )
    return render (request,"page/page_viewer.html",context)

def page_view (request,slug):
    result = list(filter(lambda x: (x["url"] == slug),FAKE_DB_PROJECTS))
    if result:
        title=result[0]["url"]
        detail=result[0]["detail"]
        context = dict (
            page_title=title,
            page_details=detail,
        )
        return render (request,"page/page_viewer.html",context)
    raise Http404('Sayfa bulunamadı...')
