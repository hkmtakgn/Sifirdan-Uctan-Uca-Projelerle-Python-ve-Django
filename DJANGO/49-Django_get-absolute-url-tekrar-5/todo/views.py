from django.shortcuts import render
from todo.models import Todo,Category
from django.shortcuts import get_object_or_404

# Create your views here.


def todo_views (request):
    todos = Todo.objects.filter(is_active=True)
    title = "Nova Team"
    context = dict (
        page_title=title,
        todos=todos,
    )
    return render (request,"todo/todo_home.html",context)

def category_detail (request,category_slug):
    category = get_object_or_404 (Category,slug=category_slug)
    todos = Todo.objects.filter(category=category)
    title = "Category Detail"
    context = dict (
        page_title=title,
        todos=todos,
    )
    return render (request,"todo/category_detail.html",context)

def todo_detail (request,id):
    todo = get_object_or_404(Todo,pk=id)
    context = dict (
        todo=todo,
        id=id,
    )
    return render (request,"todo/todo_detail.html",context)

