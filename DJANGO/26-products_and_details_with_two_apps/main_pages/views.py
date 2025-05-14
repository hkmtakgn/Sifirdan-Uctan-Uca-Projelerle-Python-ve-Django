from django.shortcuts import render
from .main_database import three_picsum

# Create your views here.


def home (request):
    page_title = "Home Page"
    context = dict (
        page_title=page_title,
        three_picsum=three_picsum,
    )
    return render (request,"main/home.html",context)
    
def contact (request):
    page_title = "Contact Page"
    context = dict (
        page_title=page_title,
    )
    return render (request,"main/contact.html",context)
    
def vision (request):
    page_title = "Vision Page"
    context = dict (
        page_title=page_title,
    )
    return render (request,"main/vision.html",context)
    