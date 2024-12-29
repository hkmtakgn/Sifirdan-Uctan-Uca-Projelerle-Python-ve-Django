from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import get_object_or_404


# Create your views here.


def todo_views (request):
    todos = Todo.objects.all()
    title = "Todos Home"
    context = dict (
        page_title=title,
        todos=todos,
        )
    return render (request,"todo/todo_home.html",context)

def todo_detail_views (request,id):
    todos = get_object_or_404(Todo,pk=id)
    title = "Todo Detail"
    context = dict (
        page_title=title,
        todos=todos,
    )

    return render (request,"todo/todo_home.html",context)

