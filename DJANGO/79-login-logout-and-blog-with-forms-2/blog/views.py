from django.shortcuts import render,redirect
from .forms.login_form import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms.register_form import RegisterForm
from django.contrib.auth.models import User
from .forms.post_form import PostForm
from blog.models import add_story_model
from django.core.paginator import Paginator
# Create your views here.


def home_views (request):
    if request.user.is_authenticated :
        context = dict ()
        return render (request, "pages/home_page.html", context)
    else :
        return redirect ( "login_views" )


def stories_views (request):
    if request.user.is_authenticated:

        items = add_story_model.objects.all()

        p_items = Paginator (items, 4)
        page_number = request.GET.get ("page")
        stories = p_items.get_page (page_number)
        
        context = dict (
            stories=stories,
        )
        return render (request, "pages/stories_page.html", context)
    else:
        messages.warning ( request, "Hikayeleri görebilmek için giriş yapın!" )
        return redirect ( "login_views" )

def login_views (request):
    if request.method == "POST":
        form = LoginForm (request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate (username=username, password=password)
            if user is not None :
                login (request, user)
                messages.info (request, "Giriş yapıldı!")
                return redirect ( "home_views" )
            else :
                form = LoginForm ()
                messages.warning ( request, "Bilgileri tekrar kontrol et!" )
                return redirect ( "login_views" )
    else:
        form = LoginForm ()
        context = dict (
            form=form,
        )
        return render (request, "pages/login_page.html", context)



def register_views (request):
    if request.method == "POST":
        form = RegisterForm (request.POST)
        if form.is_valid():
            username = request.POST.get ( "username" )
            password = request.POST.get ("password")
            confirm_password = request.POST.get ("confirm_password")
            email = request.POST.get ("email")
            confirm_email = request.POST.get ("confirm_email")
            if not password == confirm_password:
                messages.warning (request, "Şifreler aynı değil!")
                return redirect ( "register_views" )
            if not email == confirm_email:
                messages.warning (request, "Email adresleri aynı değil!")
                return redirect ( "register_views" )
            user = User.objects.filter (username=username, email=email).first ()
            if user is not None:
                login ( request, user )
                messages.success ( request, "Kullanıcı zaten kayıtlı, oturumunuz açıldı!" )
                return redirect ( "home_views" )
            else:
                username = request.POST.get ("username")
                password = request.POST.get ("password")
                user = User.objects.create (username=username, email=email)
                user.set_password (password)
                user.save ()
                form = RegisterForm (request.POST)
                form.save ()
                login ( request, user )
                messages.success ( request, "Kayıt başarıyla tamamlandı!" )
                return redirect ( "home_views" )
    else:        
        form = RegisterForm ()  
        context = dict (
            form=form,
        )
        return render (request, "pages/register_page.html", context)


def logout_views (request):
    logout (request)
    messages.success (request, "Oturum kapatıldı!")
    return redirect ( "login_views" )


def add_story (request):
    if request.method == "POST":
        form = PostForm (request.POST,request.FILES)
        if form.is_valid():
            story = form.save ()
            messages.success (request, "Story eklendi!")
        else:
            form = PostForm ()
            messages.warning (request, "Alanları doldurun!")

    form = PostForm ()
    context = dict (
        form=form,
    )
    return render ( request, "pages/add_story.html", context )

