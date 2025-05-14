from django.contrib import admin
from pages.models import Category,Tag,Developer

# Register your models here.

class AdminViews (admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]

    list_display_links = [
        "title",
        "is_active",
    ]

admin.site.register (Category,AdminViews)
admin.site.register (Tag,AdminViews)
admin.site.register (Developer,AdminViews)

