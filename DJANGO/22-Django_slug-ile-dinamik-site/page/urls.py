from django.urls import path
from page.views import (
    home,
    contact,
    vision,
    page_view,
)

urlpatterns = [
    path("",home,name="home"),
    path("contact",contact,name="contact"),
    path("vision",vision,name="vision"),
    path("<slug:slug>",page_view),
]
