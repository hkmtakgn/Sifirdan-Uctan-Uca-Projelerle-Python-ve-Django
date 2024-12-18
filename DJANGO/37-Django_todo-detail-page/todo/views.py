from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import get_object_or_404

# Create your views here.

def todo_views (request):
    todos = Todo.objects.all()
    context = dict (
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)

def todo_detail(request,id):
        todos = Todo.objects.all()
        todo = get_object_or_404(Todo,pk=id)
        context = dict (
            todos=todos,
            todo=todo,
        )
        return render (request,"todo/todo_detail.html",context)
