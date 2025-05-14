from django.contrib import admin
from app2.models import Kategori,Etiket,Gelistirici

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

admin.site.register (Kategori,AdminViews)
admin.site.register (Etiket,AdminViews)
admin.site.register (Gelistirici,AdminViews)

