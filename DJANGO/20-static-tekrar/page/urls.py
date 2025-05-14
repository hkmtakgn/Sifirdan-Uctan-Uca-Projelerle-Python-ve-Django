from django.urls import path
from page.views import (
    home,
    contact,
    aboutus,
)

urlpatterns = [
    path ("",home),
    path ("contact",contact),
    path ("aboutus",aboutus),
]
