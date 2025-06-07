from django.contrib import admin
from xdevs.models import Web_Pages, W_Languages, Developer

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]

    list_display_links = [
        "title",
        "is_active",
    ]


admin.site.register(Web_Pages, PageAdmin)


@admin.register(W_Languages)
class LangAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
    ]
