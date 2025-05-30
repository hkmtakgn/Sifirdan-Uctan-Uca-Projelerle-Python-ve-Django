from django.shortcuts import render,get_object_or_404
from todo.models import Todo

# Create your views here.

def todo_views (request):
    todos = Todo.objects.all()
    context = dict (
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)


def todo_detail (request,id):
    todo = get_object_or_404(Todo,pk=id)
    context = dict (
        todo=todo,
    )
    return render (request,"todo/todo_detail.html",context)

