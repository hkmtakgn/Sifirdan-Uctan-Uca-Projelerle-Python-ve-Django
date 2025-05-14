from django.urls import path
from app2.views import home_views,kat_views,gelis_views,tag_set_views



app_name="app2"
urlpatterns = [
    path("",home_views,name="home"),
    path("<slug:kategori_slug>/",kat_views,name="kategori"),
    path("<slug:kategori_slug>/<int:id>/",gelis_views,name="gelistirici"),
    path("<slug:kategori_slug>/<slug:tag_slug>/",tag_set_views,name="tag_set"),
]


