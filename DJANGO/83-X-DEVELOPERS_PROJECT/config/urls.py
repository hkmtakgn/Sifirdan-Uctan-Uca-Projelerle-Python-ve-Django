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
from xdevs.views import (x_home_views, web_views, lang_views, dev_details)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", x_home_views, name="x_home"),
    path("<slug:page_slug>/", web_views, name="main_pages"),
    path("<slug:page_slug>/<slug:lang_slug>/", lang_views, name="langs"),
    path("<int:id>", dev_details, name="dev"),
    path("add-page/", web_views, name="add_page"),
]
