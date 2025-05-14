from django.contrib import admin
from todo.models import Todo,Category

# Register your models here.

class Todo_View_Opt (admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "is_active",
        "created_at",
        "updated_at",
    ]

class Category_view_opt (admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]


admin.site.register(Todo,Todo_View_Opt)

admin.site.register(Category,Category_view_opt)

