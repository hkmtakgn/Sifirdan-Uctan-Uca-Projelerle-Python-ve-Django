from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import get_object_or_404


# Create your views here.


def todo_views (request,id=None):
    if not id:
        todos = Todo.objects.filter(is_active=True)
        title = "Todo Home Page"
        context = dict (
            page_title=title,
            todos=todos,
        )
    elif id:
        todoo = get_object_or_404(Todo,pk=id)
        title = "Todo Detail"
        context = dict (
            todoo=todoo,
            page_title=title,
        )
    return render (request,"todo/todo_home.html",context)

