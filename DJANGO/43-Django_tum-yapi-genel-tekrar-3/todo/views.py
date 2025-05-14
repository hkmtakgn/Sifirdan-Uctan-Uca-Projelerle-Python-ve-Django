from django.shortcuts import render
from todo.models import Todo,Category
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.


def todo_views (request):
    todos = Todo.objects.all()
    title = "Todos Home Page"
    context = dict (
        page_title=title,
        todos=todos,
    )
    return render (request,"todo/todo_home.html",context)

def todo_detail (request,id):
    todo = get_object_or_404(Todo,pk=id)
    title = "Todos Detail Page"
    context = dict (
        page_title=title,
        todo=todo,
    )
    return render (request,"todo/todo_detail.html",context)


def category_view (request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    todos = Todo.objects.filter(category=category)
    title = "Category Detail Page"
    context = dict (
        page_title=title,
        category=category,
        todos=todos,
    )
    return render (request,"todo/category_detail.html",context)

def page_views (request,slug):
    if slug == "contact":
        todos = Todo.objects.filter(is_active=True)
        title = "Contact Page"
        context = dict (
            page_title=title,
            todos=todos,
        )
    elif slug == "vision":
        title = "Vision Page"
        context = dict (
            page_title=title,
        )
    else:
        raise Http404 ("Sayfa bulunamadı...")

    return render (request,"pages/page_viewer.html",context)
    
