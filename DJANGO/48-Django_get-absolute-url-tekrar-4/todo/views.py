from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import get_object_or_404

# Create your views here.


def todo_views (request,id=None):
    if not id:
        todos = Todo.objects.all()
        title = "Todo Home"
        context = dict (
            page_title=title,
            todos=todos,
        )
        return render (request,"todo/todo_home.html",context)
    elif id:
        todo = get_object_or_404(Todo,pk=id)
        title = "Todo Detail Page"
        context = dict (
            page_title=title,
            todo=todo,
        )
        return render (request,"todo/todo_detail.html",context)
    
    