from django.contrib import admin
from todo.models import Todo,Category,Tag

# Register your models here.

class TodoViewsOpt (admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
    )

    list_display_links = (
        "title",
        "is_active",
    )

admin.site.register(Todo,TodoViewsOpt)
admin.site.register(Category,TodoViewsOpt)
admin.site.register(Tag)

