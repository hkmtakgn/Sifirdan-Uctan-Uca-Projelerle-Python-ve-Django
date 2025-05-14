from django.shortcuts import render
from .fake_db.pages import FAKE_DB
from django.http import Http404


# Create your views here.

lorem_pics = [
    f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)
]

def home (request):
    title = "Home Page"
    context = dict (
        page_title=title,
    )
    return render (request,"page/home.html",context)

def contact (request):
    users = [
        "o.yildirim@hotmail.com",
        "na.duman@outlook.com",
        "z.usta@yahoo.com",
        "hikmetakgun94@gmail.com",
    ]
    title = "Contact"
    context = dict (
        page_title=title,
        users=users,
    )
    return render (request,"page/contact.html",context)

def vision (request):
    title = "Vision"
    context = dict (
        page_title=title,
        lorem_pics=lorem_pics,
    )
    return render (request,"page/vision.html",context)

def page_view (request,slug):
    result = list(filter(lambda x: (x["url"] == slug),FAKE_DB))
    if result:
        context = dict (
            page_title=result[0]["url"].upper(),
            page_details=result[0]["detail"]
        )
        return render (request,"page/page_viewer.html",context)
    raise Http404("Sayfa bulunamadı...")
