from django.contrib import admin
from developers.models import Developers,Categories,Tag

# Register your models here.

class Admin_Views (admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]


admin.site.register (Developers,Admin_Views)
admin.site.register (Categories,Admin_Views)
admin.site.register (Tag,Admin_Views)
