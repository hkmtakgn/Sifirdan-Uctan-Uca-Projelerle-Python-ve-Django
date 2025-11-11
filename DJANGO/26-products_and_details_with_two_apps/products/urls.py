from django.urls import path
from .views import pro_views,detail_pro_view

urlpatterns = [
    path("",pro_views),
    path("detail-product/<int:product_id>/",detail_pro_view,name="detail_pro_name"),
]
