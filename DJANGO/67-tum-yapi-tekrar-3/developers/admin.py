from django.contrib import admin
from developers.models import Developer,Category,Tag

# Register your models here.

class admin_views (admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
    ]

admin.site.register (Developer,admin_views)
admin.site.register (Category,admin_views)
admin.site.register (Tag,admin_views)


