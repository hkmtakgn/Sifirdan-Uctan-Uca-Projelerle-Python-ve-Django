from django.shortcuts import render,redirect
from .form_views.login_form import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import Http404
from .form_views.register_form import RegisterForm
from django.contrib.auth.models import User
from .form_views.blog_post import PostForm
from pages.models import blog_post
# Create your views here.
from django.core.paginator import Paginator


def home_views (request) :
    title = "Home"
    posts_data = blog_post.objects.all ()
    x_posts = Paginator (posts_data, 4)
    page_number = request.GET.get ("page")
    posts = x_posts.get_page (page_number)

    context = dict (
        page_title=title,
        posts=posts,
    )
    return render ( request, "main/home_page.html", context)

def login_views (request) :
    title = "Login"
    if request.method == "POST":
        log_form = LoginForm (request.POST)
        if log_form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate (username=username, password=password)
            if user is not None:
                login (request, user)
                messages.info (request,"Giriş başarılı!")
                return redirect ("home_views")
            else:
                messages.warning (request,"Bilgiler hatalı!")
                return redirect ("login_views")

    else:
        log_form = LoginForm ()
    context = dict (
        page_title=title,
        log_form=log_form,
    )
    return render (request, "main/login_page.html", context)


def logout_views (request) :
    logout (request)
    messages.success (request, "Çıkış başarılı!")
    return redirect ("login_views")



def blog_views(request):
    title = "Blog Page"

    if request.method == "POST":
        if request.user.is_authenticated:
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Gönderi başarıyla eklendi!")
                return redirect("blog_views")
        else:
            return redirect("login_views")
    else:
        if request.user.is_authenticated:
            form = PostForm()
        else:
            return redirect("login_views")

    context = dict(
        page_title=title,
        form=form,
    )
    return render(request, "main/blog_page.html", context)
    

def register_views (request) :
    title = "Register"
    if request.method == "POST":
        reg_form = RegisterForm (request.POST)
        if reg_form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate (username=username, password=password)
            if user is not None:
                login (request,user)
                messages.success (request,"Kullancı zaten kayıtlı! Oturum açıldı.")
                return redirect ("home_views")
            else:
                username = request.POST.get ("username")
                password = request.POST.get ("password")
                user = User.objects.create (username=username)
                user.set_password (password)
                user.save ()
                messages.success (request, "Kayıt başarılı!")
                login (request,user)
                return redirect ("home_views")
        else:
            messages.warning (request, "Bilgileri kontrol et!")
            return redirect ("register_views")

    else:
        reg_form = RegisterForm ()
    context = dict (
        page_title=title,
        reg_form=reg_form,
    )
    return render (request, "main/register_page.html", context)

