from django.shortcuts import render

# Create your views here.

def home (request):
    title = "Home Page"
    context = dict (
        page_title=title,
    )
    return render (request,"page/home.html",context)

def contact (request):
    title = "Contact"
    context = dict (
        page_title=title,
    )
    return render (request,"page/contact.html",context)

def aboutus (request):
    title = "About Us"
    context = dict (
        page_title=title,
    )
    return render (request,"page/aboutus.html",context)
