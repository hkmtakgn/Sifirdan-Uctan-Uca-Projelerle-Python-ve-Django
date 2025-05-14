from django.shortcuts import render
from todo.models import Todo

# Create your views here.

def todo_views (request):
    todos = Todo.objects.all()
    active_todo = Todo.objects.filter(is_active=True)
    title = "Todo List"
    context = dict (
        page_title=title,
        todos=todos,
        active_todo=active_todo,
    )
    return render (request,"page_viewer/page_views.html",context)
