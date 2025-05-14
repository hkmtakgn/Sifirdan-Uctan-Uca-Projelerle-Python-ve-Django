from django.contrib import admin
from todo.models import Todo,Category

# Register your models here.

class Todo_list_view (admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]

    list_display_links = [
        "title",
        "is_active",
    ]


admin.site.register(Todo,Todo_list_view)
admin.site.register(Category,Todo_list_view)

