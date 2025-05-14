from django.urls import path
from products.views import pro_views

urlpatterns = [
    path('',pro_views,name='pro_views'),
    path('<slug:pro_slug>/',pro_views,name='pro_slug_views'),
]

