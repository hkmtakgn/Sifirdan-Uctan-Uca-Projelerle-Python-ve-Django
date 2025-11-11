from django.shortcuts import render

# Create your views here.

def home(request):
    context = dict ()
    return render (request,"page/home.html",context)
