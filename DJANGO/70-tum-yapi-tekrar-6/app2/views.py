from django.shortcuts import render,get_object_or_404
from app2.models import Kategori,Etiket,Gelistirici
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/admin/login/")
def home_views (request):
    title = "Cinsiyet Seçin!"
    kategoriler = Kategori.objects.filter (is_active=True)
    context = dict (
        page_title=title,
        items=kategoriler,
    )
    return render (request,"app2/todo_home.html",context)

@login_required(login_url="/admin/login/")
def kat_views (request,kategori_slug):
    kategori = get_object_or_404 (Kategori,slug=kategori_slug,is_active=True)
    gelistiriciler = Gelistirici.objects.filter (etiket__kategori=kategori,is_active=True).distinct()
    title = kategori.title
    context = dict (
        page_title=title,
        items=gelistiriciler,
    )
    return render (request,"app2/kategoriler.html",context)

@login_required(login_url="/admin/login/")
def gelis_views (request,kategori_slug,id):
    item = get_object_or_404 (Gelistirici,pk=id)
    title = item.title + " kişisinin seçtikleri"
    context = dict (
        page_title=title,
        items=item.etiket.all,
    )
    return render (request,"app2/gelistirici.html",context)

@login_required(login_url="/admin/login/")
def tag_set_views (request,kategori_slug,tag_slug):
    kat = get_object_or_404 (Kategori,slug=kategori_slug)
    etikets = get_object_or_404 (Etiket,slug=tag_slug,kategori=kat)
    title = etikets.title + " seçen kişiler"
    context = dict (
        page_title=title,
        items=etikets.gelistirici_set.all,
    )
    return render (request,"app2/set_tags.html",context)

