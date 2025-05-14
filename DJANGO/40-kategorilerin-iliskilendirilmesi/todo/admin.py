from django.contrib import admin
from todo.models import Todo
from todo.models import Category

# Register your models here.

class Todo_list_view (admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
        "category",
    ]

    list_display_links = [
        "title",
        "category",
    ]


admin.site.register(Todo,Todo_list_view)
admin.site.register(Category)

