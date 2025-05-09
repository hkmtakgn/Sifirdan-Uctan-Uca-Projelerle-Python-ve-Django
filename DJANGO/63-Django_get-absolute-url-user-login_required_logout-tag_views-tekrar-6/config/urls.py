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
from todo.views import (
    todo_views,
    todo_detail_views,
    category_views,
    category_todo_detail_views,
    logout_views,
    tag_views,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",todo_views,name="home"),
    path("todos/<int:id>/",todo_detail_views,name="todo_detail"),
    path("categories/<slug:category_slug>/",category_views,name="category_views"),
    path("categories/<slug:category_slug>/todos/<int:id>/",category_todo_detail_views,name="category_todo_detail_views"),
    path("logout/",logout_views,name="logout_views"),
    path("tag/<slug:tag_slug>/",tag_views,name="tag_views"),
]

