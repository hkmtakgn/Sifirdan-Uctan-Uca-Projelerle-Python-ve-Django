from django.contrib import admin
from pages.models import Todo,Category


class TodoAdmin (admin.ModelAdmin):
    list_display = ("title","category","is_active")
    list_display_links = ("title","category","is_active")

class CategoryAdmin (admin.ModelAdmin):
    list_display = ("title","is_active")
    list_display_links = ("title","is_active")


admin.site.register(Todo,TodoAdmin)
admin.site.register(Category,CategoryAdmin)

