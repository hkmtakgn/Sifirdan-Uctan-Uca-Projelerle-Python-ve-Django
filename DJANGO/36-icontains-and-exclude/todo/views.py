from django.shortcuts import render
from todo.models import Todo

# Create your views here.

def todo_views (request):
    todos = Todo.objects.all()
    actives = todos.filter(is_active=True)
    passives = todos.filter(is_active=False)
    context = dict (
        todos=todos,
        actives=actives,
        passives=passives,
    )
    return render (request,"todo/todo_views.html",context)

