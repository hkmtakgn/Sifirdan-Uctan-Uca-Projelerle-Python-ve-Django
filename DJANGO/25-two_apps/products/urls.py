from django.urls import path
from .views import pro_view,mini_pro_view

urlpatterns = [
    path("",pro_view,name="products"),
    path("mini-products/",mini_pro_view,name="mini-products"),
]
