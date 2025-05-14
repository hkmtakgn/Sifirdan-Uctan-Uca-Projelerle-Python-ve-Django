from django.shortcuts import render
from todo.models import Todo,Category
from django.shortcuts import get_object_or_404

# Create your views here.


def todo_views (request):
    todos = Todo.objects.all()
    context = dict (
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)

def todo_detail_views (request,id):
    todo_detail = get_object_or_404(Todo,pk=id)
    context = dict (
        todo_detail=todo_detail,
    )
    return render (request,"todo/todo_detail_views.html",context)

def category_views (request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
    )
    context = dict (
        category=category,
        todos=todos,
    )
    return render (request,"todo/todo_views.html",context)

