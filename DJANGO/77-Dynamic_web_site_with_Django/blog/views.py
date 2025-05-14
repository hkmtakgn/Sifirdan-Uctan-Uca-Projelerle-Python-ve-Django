from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.


def home_views (request):
    context = dict ()
    return render (request, "blog/home.html", context)


def login_views (request):
    if request.method == "POST":
        username = request.POST.get ("username")
        password = request.POST.get ("password")
        user = authenticate (User,username=username, password=password)
        if user is not None:
            print (user)
            login (request,user)
            messages.success(request, f"Hoş geldin, {username}!")
            return redirect ("home")
        else:
            messages.warning (request, f"Kullanıcı adı veya şifre yanlış!")
    context = dict ()
    return render (request, "blog/login_page.html", context)


def blog_views (request):
    if request.user.is_authenticated:
        context = dict ()
        return render (request, "blog/blog_page.html", context)
    else:
        raise Http404("Sayfa bulunamadı!")


def logout_views (request):
    logout (request)
    return redirect ("login_views")

def register_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")
        confirm_email = request.POST.get("confirm_email")

        # Email ve şifre doğrulama (isteğe bağlı)
        if password != confirm_password:
            messages.warning (request, "Şifreler uyuşmuyor.")
            return redirect("register_views")
        
        if email != confirm_email:
            messages.warning (request, "Email adresleri uyuşmuyor.")
            return redirect("register_views")

        # Kullanıcı zaten var mı kontrolü
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request, f"Kayıt başarılı, hoş geldin {username}!")
            return redirect("home")
        else:
            login (request, user)
            messages.info (request, f"Bu kullanıcı zaten mevcut. Tekrar hoşgeldin {username}!")
            return redirect("home")

    return render(request, "blog/register_page.html", {})
