from django.urls import path
from page.views import (
    home,
    contact,
)

urlpatterns = [
    path ("",home),
    path ("contact",contact),
]
