from django.contrib import admin
from developers.models import Developer,Category,Tag


# Register your models here.

class AdminViews (admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
    ]

admin.site.register (Developer,AdminViews)
admin.site.register (Category,AdminViews)
admin.site.register (Tag,AdminViews)

