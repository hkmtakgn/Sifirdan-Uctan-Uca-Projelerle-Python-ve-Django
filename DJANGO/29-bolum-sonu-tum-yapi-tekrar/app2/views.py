from django.shortcuts import render

# Create your views here.

def app2_views (request):
    title = "App2 Home Page"
    context = dict (
        page_title=title,
    )
    return render (request,"pages/app2_home.html",context)

def app2_hub_views (request,slug):
    if slug == "app2_hub":
        title = "App2 Subordinate Page"
        context = dict (
            page_title=title,
        )
        return render (request,"pages/app2_hub.html",context)
    