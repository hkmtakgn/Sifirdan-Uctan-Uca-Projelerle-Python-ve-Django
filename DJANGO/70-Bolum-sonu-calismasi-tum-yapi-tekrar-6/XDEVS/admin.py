from django.contrib import admin
from XDEVS.models import Category,Developer,Tag

# Register your models here.

class AdminViews (admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
    ]


admin.site.register (Category,AdminViews)
admin.site.register (Developer,AdminViews)
admin.site.register (Tag,AdminViews)
