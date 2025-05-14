from django.urls import path
from .views import app1_views,app1_sub_views

urlpatterns = [
    path("", app1_views, name="app1_home"),
    path("/<slug:slug>/",app1_sub_views,name="slug_views"),
]
