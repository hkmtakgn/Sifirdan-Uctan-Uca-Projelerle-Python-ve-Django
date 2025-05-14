from django.urls import path
from .views import app2_views,app2_hub_views

urlpatterns = [
    path("",app2_views,name="app2_home"),
    path("/<slug:slug>/",app2_hub_views,name='app2_view'),
]
