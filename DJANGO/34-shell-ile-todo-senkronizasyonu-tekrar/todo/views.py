from django.shortcuts import render
from todo.models import Todo

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    active_todo = todos.filter(is_active=True)
    context = dict (
        todos=todos,
        active_todo=active_todo,
    )
    return render (request,"page/home.html",context)
