from django.shortcuts import render

# Create your views here.

def home (request):
    paragraph = "Lorem ipsum dolor!"
    context = dict (
        paragraph = paragraph,
    )
    return render (request,"page/home.html",context)

def contact (request):
    return render (request,"page/contact.html",{})
