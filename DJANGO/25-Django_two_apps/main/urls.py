from django.urls import path
from .views import (
    home,
    vision,
    contact
)

urlpatterns = [
    path("",home,name="home"),
    path("vision",vision,name="vision"),
    path("contact",contact,name="contact"),
]
