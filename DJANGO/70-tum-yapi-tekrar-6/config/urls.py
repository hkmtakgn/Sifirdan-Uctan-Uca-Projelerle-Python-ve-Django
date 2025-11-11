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
from django.urls import path,include
from pages.views import (
    home_views,
    cat_views,
    tag_views,
    dev_views,
    logout_views,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("" , home_views , name="home_views"),
    path ("app2/",include('app2.urls',namespace="app2"),),
    path ("<int:id>/",dev_views,name="dev_views"),
    path ("<slug:cat_slug>/",cat_views,name="cat_views"),
    path ("<slug:cat_slug>/<slug:tag_slug>/",tag_views,name="tag_views"),
    path ("/logout/",logout_views,name="logout_views"),
]

