from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate
from xdevs.models import Developer
from django.core.paginator import Paginator


# Create your views here.
def home_views (request):
    if request.user.is_authenticated:
        x_developers = Developer.objects.filter (is_active=True)
        xdevs = Paginator (x_developers,3)
        page_number = request.GET.get ("page")
        developers = xdevs.get_page (page_number)
        context = dict (
            developers=developers,
        )
        return render (request, "pages/home.html", context)
    else:
        return redirect ("login_views")

def logout_views (request):
    context = dict ()
    logout (request)
    return render (request, "pages/login.html", context)


def login_views (request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        login_user = authenticate (request,username=username, password=password)
        if login_user:
            login (request,login_user)
            messages.success (request, f"{username} is login!")
        else:
            messages.warning (request, f"Bilgiler hatalı!")
            return redirect ("login_views")
        context = dict ()
        return redirect ("home")
    context = dict ()
    return render (request,"pages/login.html",context)



def register_views (request):
    if request.method == "POST":
        username = request.POST.get ("username")
        user_email = request.POST.get ("email")
        confirm_user_email = request.POST.get ("confirm_email")
        user_password = request.POST.get ("password")
        confirm_user_password = request.POST.get ("confirm_password")
        exists_user = User.objects.filter (username=username, email=user_email).first ()
        if not exists_user:
            if user_email == confirm_user_email and user_password == confirm_user_password:
                user = User.objects.create (username=username, email=user_email, is_active=True)
                user.set_password (user_password)
                user.save ()
                messages.success (request, f"Kayıt başarılı!")
                return redirect ("home")
        else:
            exists_user = authenticate (request,username=username,password=user_password)
            if exists_user:
                messages.success (request,"Kullanıcı zaten kayıtlı!")
                login (request,exists_user)
                return redirect ("home")
            else:
                messages.warning (request, f"Bilgiler hatalı!")
                return redirect ("register")
    context = dict ()
    return render (request,"pages/register.html", context)

