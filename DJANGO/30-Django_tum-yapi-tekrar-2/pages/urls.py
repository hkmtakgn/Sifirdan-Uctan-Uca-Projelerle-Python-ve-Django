from django.urls import path
from .views import page_views

urlpatterns = [
    path("",page_views,name="home"),
    path("<slug:slug>/",page_views,name="slug_views"),
]
