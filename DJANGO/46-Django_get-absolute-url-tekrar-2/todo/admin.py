from django.contrib import admin
from todo.models import Todo

# Register your models here.

class TodoAdmin (admin.ModelAdmin):
    list_display = ("title","is_active")
    list_display_links = ("title","is_active")


admin.site.register(Todo,TodoAdmin)

