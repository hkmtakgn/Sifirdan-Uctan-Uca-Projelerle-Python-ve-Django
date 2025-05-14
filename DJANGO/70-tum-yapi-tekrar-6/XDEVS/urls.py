from django.urls import path 
from XDEVS.views import x_views




urlpatterns = [
    path ( "",x_views,name='x_views' ),
    path ( "<slug:cat_slug>/",x_views,name='cat_views' ),
    path ( "<slug:cat_slug>/<int:id>/",x_views,name='detail_views' ),
    path ( "<slug:cat_slug>/<int:id>/<slug:tag_slug>/",x_views,name='tag_views' ),
]

