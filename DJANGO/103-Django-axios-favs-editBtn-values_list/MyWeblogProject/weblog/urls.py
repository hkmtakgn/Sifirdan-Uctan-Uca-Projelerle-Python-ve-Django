from django.urls import path
from weblog.views import general_views, post_detail_views, login_views, add_fav_views, edit_post

app_name = 'weblog'

urlpatterns = [
    path("", general_views, name="home"),
    path("edit-post/<slug:post_slug>/", edit_post, name="edit-post"),
    path("add-fav/", add_fav_views, name="add-fav"),
    path("<slug:page_slug>/", general_views, name="page-detail"),
    path("posts/<int:id>", post_detail_views, name="post-detail"),
    path("/login/", login_views, name="login"),
]
