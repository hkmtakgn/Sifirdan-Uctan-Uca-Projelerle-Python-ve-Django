"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from blog.views import (
    home_views,
    stories_views,
    login_views,
    register_views,
    logout_views,
    add_story,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path ( "", home_views, name="home_views" ),
    path ( "login/", login_views, name="login_views" ),
    path ( "logout/", logout_views, name="logout_views" ),
    path ( "register/", register_views, name="register_views" ),
    path ( "stories/", stories_views, name="stories_views" ),
    path ( "add-story/", add_story, name="add_story"),
] + static ( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

