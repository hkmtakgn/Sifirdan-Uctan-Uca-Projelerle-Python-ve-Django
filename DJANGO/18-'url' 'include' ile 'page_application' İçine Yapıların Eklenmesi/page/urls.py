from django.urls import path
from .views import (
    home,
    contact,
    aboutus,
)


urlpatterns = [
    path ("",home),
    path ("contact",contact),
    path ("about-us",aboutus),
]
