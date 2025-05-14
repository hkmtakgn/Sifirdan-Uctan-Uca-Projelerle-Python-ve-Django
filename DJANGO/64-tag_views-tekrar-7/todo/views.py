from django.shortcuts import render
from todo.models import Todo,Category,Tag
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.

@login_required(login_url='/admin/login/')
def todo_views (request):
    todos = Todo.objects.filter(user=request.user)
    title = "Nova Team"
    context = dict (
        page_title=title,
        todos=todos,
    )
    return render (request,"todo/todo_home.html",context)

@login_required(login_url='/admin/login/')
def todo_detail_views (request,id):
    todo = get_object_or_404(Todo,pk=id,user=request.user)
    title = "User Detail"
    context = dict (
        todo=todo,
        page_title=title,
    )
    return render (request,"todo/todo_detail.html",context)

@login_required(login_url='/admin/login/')
def category_views (request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    cat_todo = Todo.objects.filter(category=category,user=request.user)
    title = "Category Detail"
    context = dict (
        page_title=title,
        cat_todo=cat_todo,
    )
    return render (request,"todo/todo_detail.html",context)

@login_required(login_url='/admin/login/')
def view_todo_in_category (request,id,category_slug):
    todo = get_object_or_404(Todo,pk=id,category__slug=category_slug,user=request.user)
    title = "User Detail"
    context = dict (
        todo=todo,
        page_title=title,
    )
    return render (request,"todo/todo_detail.html",context)

def logout_views (request):
    logout(request)
    return redirect ('home')


@login_required(login_url='/admin/login/')
def tag_views (request,tag_slug):
    tag = get_object_or_404 (Tag,slug=tag_slug)
    title = tag.title.capitalize()
    context = dict (
        page_title=title,
        todos=tag.todo_set.filter(user=request.user),
        tag=tag,
    )
    return render (request,"todo/todo_home.html",context)

