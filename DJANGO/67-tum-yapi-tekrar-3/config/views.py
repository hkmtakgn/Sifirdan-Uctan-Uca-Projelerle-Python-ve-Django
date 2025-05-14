from django.shortcuts import render
from pages.views import home

# Create your views here.


def main_views (request):
    if request.path == "/":
        path = '/'
        return home(request,path)
    elif request.path == "/vision/":
        path = "vision"
        return home(request,path)
    elif request.path == "/contact/":
        path = "contact"
        return home(request,path)

