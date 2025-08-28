"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from weblog.views import home_views, add_post_views, delete_item, edit_item, favorites_views, add_favs

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views, name="home"),
    path("add-post/", add_post_views, name="add_post"),
    path("favorites/", favorites_views, name="favorites"),
    path("delete/<int:id>", delete_item, name="delete_item"),
    path("edit/<int:id>", edit_item, name="edit_item"),
    path("favs/<int:id>", add_favs, name="favs"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
