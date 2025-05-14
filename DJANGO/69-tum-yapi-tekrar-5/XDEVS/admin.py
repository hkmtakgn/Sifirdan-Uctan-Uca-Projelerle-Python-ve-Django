from django.contrib import admin
from XDEVS.models import User,Category,Tag

# Register your models here.

class UserViews (admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]

    list_display_links = [
        "title",
        "is_active",
    ]


admin.site.register (User,UserViews)
admin.site.register (Category,UserViews)
admin.site.register (Tag,UserViews)

