from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request,"pages/home.html",{})

def vision (request):
    return render (request,"pages/vision.html",{})

def contact (request):
    return render (request,"pages/contact.html",{})
