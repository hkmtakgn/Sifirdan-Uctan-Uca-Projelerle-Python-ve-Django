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
from security_control.views import (
    home_views,
    visitor_views,
    subcontractor_views,
    visitor_register_views,
    visitor_details_views,
    subcontractor_register_views,
    subcontractor_details_views,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views, name="home"),
    path("visitor/", visitor_views, name="visitor"),
    path("subcontractor/", subcontractor_views, name="subcontractor"),
    path("visitor-register/", visitor_register_views, name="visitor-register"),
    path("subcontractor-register/",
         subcontractor_register_views,
         name="subcontractor-register"),
    path("visitor/<int:id>/", visitor_details_views, name="visitor-detail"),
    path("subcontractor/<int:id>/",
         subcontractor_details_views,
         name="subcontractor-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
