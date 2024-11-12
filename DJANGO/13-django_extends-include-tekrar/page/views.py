from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request,"page/home.html",{})

def aboutus (request):
    return render (request,"page/aboutus.html",{})
def contact (request):
    return render (request,"page/contact.html",{})
