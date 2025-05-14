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
from .views import main_views
from developers.views import dev_views
from developers.views import tag_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main_views),
    path("vision/",main_views,name="vision"),
    path("contact/",main_views,name="contact"),
    path('products/',include('products.urls')),
    path('products/<slug:pro_slug>/',include('products.urls')),
    path('developers/',dev_views,name='dev_views'),
    path('developers/<int:id>/',dev_views,name='dev_details'),
    path('tag/<slug:tag_slug>/',tag_views,name='tag_views'),
]



