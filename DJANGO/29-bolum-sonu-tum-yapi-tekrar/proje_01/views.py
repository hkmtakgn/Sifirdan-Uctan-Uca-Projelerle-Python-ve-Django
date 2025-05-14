from django.shortcuts import render

def views (request):
    title = "Home Page"
    context = dict (
        page_title=title,
    )
    return render (request,"pages/home.html",context)
