from django.contrib import admin
from developers.models import Tag,Category,Developer



# Register your models here.

class Views (admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
    ]


admin.site.register (Tag,Views)
admin.site.register (Developer,Views)
admin.site.register (Category,Views)

