from django.shortcuts import render
from todo.models import Todo,Category
from django.shortcuts import get_object_or_404
# Create your views here.

def category_views (request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
    )
    context = dict (
        todos=todos,
        category=category,
    )
    return render (request,"todo/todo_views.html",context)


def todo_views (request):
    todos = Todo.objects.all()
    context = dict (
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)

def todo_detail (request,id):
    context = dict (
        todo = get_object_or_404(Todo,pk=id),
    )
    return render (request,"todo/todo_detail.html",context)
    

