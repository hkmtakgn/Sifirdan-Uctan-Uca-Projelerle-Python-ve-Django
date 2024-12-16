from django.shortcuts import render
from todo.models import Todo

# Create your views here.

def views (request):
    todos = Todo.objects.all()
    context = dict (
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)

