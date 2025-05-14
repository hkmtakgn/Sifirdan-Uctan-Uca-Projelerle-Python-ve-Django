from django.shortcuts import render,get_object_or_404,redirect
from pages.models import Page
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.urls import reverse

# Create your views here.

@login_required (login_url="/admin/login/")
def page_views (request,page_slug=None):
    admin_users = User.objects.all ()
    if request.user in admin_users:
        if not page_slug and request.path == "/":
            return redirect('ana-sayfa/')
        if page_slug == "todo":
            return redirect (reverse("todo:todo_home"))
        elif page_slug:
            page = get_object_or_404 (Page,slug=page_slug)
        context = dict (
            page=page,
        )
        return render (request,"page/page_views.html",context)
    else:
        return redirect('ana-sayfa')


def logout_view (request):
    logout (request)
    return render (request,'page/login_page.html')

def login_view (request):
    if request.method == "POST":
        post_user = request.POST.get ("username")
        post_password = request.POST.get ("password")
        user = authenticate (username=post_user,password=post_password)

        if user:
            login (request,user)
            return redirect ("home")
        else:
            context = dict ()
            return render(request, "page/login_page.html", context)
    else:
        return render ("page/login_page.html",{})
    
