from django.urls import path
from weblog.views import general_views, post_detail_views, login_views, fav_update_views

app_name = 'weblog'

urlpatterns = [
    path("", general_views, name="home"),
    path("fav-update/", fav_update_views, name="fav-update"),
    path("<slug:page_slug>/", general_views, name="page-detail"),
    path("posts/<int:id>", post_detail_views, name="post-detail"),
    path("/login/", login_views, name="login"),
]
