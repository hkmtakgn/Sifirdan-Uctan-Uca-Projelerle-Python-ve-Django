from django.shortcuts import render

# Create your views here.

def app1_views (request):
        title = "App1 Home Page"
        context = dict (
                page_title=title,
        )
        return render(request,"pages/app1_home.html",context)

def app1_sub_views (request,slug):
        if slug == "app1_sub":
                title = "App1 Subordinate Page"
                context = dict (
                        page_title=title,
                )
                return render (request,"pages/app1_sub.html",context)
        