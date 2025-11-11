from django.shortcuts import render
from todo.models import Todo,Category
from django.shortcuts import get_object_or_404

# Create your views here.


def todo_views (request):
    todos = Todo.objects.all()
    title = "Nova Team"
    context = dict (
        page_title=title,
        todos=todos,
    )
    return render (request,"todo/todo_home.html",context)

def todo_detail_views (request,id,category_slug):
    todo = get_object_or_404(Todo,pk=id,category__slug=category_slug)
    title = "User Detail"
    context = dict (
        todo=todo,
        page_title=title,
    )
    return render (request,"todo/todo_detail.html",context)


def category_views (request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    cat_todo = Todo.objects.filter(category=category)
    title = "Category Detail"
    context = dict (
        page_title=title,
        cat_todo=cat_todo,
    )
    return render (request,"todo/todo_detail.html",context)


