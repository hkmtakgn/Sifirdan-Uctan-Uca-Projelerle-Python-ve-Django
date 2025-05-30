"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import todo_views,todo_detail_views,category_views,todo_detail_views_category,logout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",todo_views,name="home"),
    path("todos/<int:id>/",todo_detail_views,name="todo_detail"),
    path("categories/<slug:category_slug>/",category_views,name="category_views"),
    path("categories/<slug:category_slug>/todos/<int:id>/",todo_detail_views_category,name="todo_detail_views_category"),
    path ("logout/",logout_views,name="logout"),
]


