from django.shortcuts import render,redirect
from django.urls import reverse
from pages.models import Todo
from django.shortcuts import get_object_or_404


# Create your views here.


def page_views (request,slug=None):
    if not slug:
        todos = Todo.objects.all()
        title = "Home Page"
        context = dict (
            page_title=title,
            todos=todos,
        )
    elif slug == "vision":
        title = "Vision Page"
        context = dict (
            page_title=title,
        )
    elif slug == "contact":
        title = "Contact Page"
        context = dict (
            page_title=title,
        )
    return render (request,"pages/page_viewer.html",context)    

def todo_detail (request,id):
    todo = get_object_or_404(Todo,pk=id)
    title = "Todo Detail"
    context = dict (
        page_title=title,
        todo=todo,
    )
    return render (request,"pages/todo_detail.html",context)

