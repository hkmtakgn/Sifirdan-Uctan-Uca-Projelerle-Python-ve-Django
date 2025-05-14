from django.urls import path
from todo.views import todo_views,todo_manager

app_name = "todo"
urlpatterns = [
    path ("", todo_views, name="todo_home"),
    path ("delete-item/", todo_manager, name="delete-item"),
    path ("todo_mng/", todo_manager, name="todo_mng"),

]

