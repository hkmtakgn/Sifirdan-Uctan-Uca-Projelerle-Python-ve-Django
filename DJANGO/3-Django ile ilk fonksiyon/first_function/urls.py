"""
URL configuration for first_function project.

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
from django.http import HttpResponse #HttpResponse class'ı import edildi

def home (request): #home fonksiyonu tanımlandı reqeust parametresi ile isteklerin gelmesini sağladık
    return HttpResponse("Anasayfaya hoşgeldiniz..") #HttpRespone ile bir http yanıtı döndürüldü

urlpatterns = [ # urlpatterns listesinde arar ve eşleşen bir yol bulursa, o yolla ilişkili görünüm fonksiyonunu çağırır.
    path("home-page/",home), #path ile anasayfa url'si tanımlandı ve home fonksiyonu çağırıldı
    path('admin/', admin.site.urls), #path ile admin url'si tanımlandı ve admin.site.urls ile admin sayfasına eriş
]
