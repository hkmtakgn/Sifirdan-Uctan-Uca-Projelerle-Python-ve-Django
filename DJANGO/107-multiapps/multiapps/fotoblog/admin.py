from django.contrib import admin
from fotoblog.models import Page, Post, FavPost, PageLogo


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register(FavPost)
class FavAdmin(admin.ModelAdmin):
    list_display = [
        "post_title",
        "is_selected",
    ]

    def post_title(self, obj):
        return obj.post.title


@admin.register(PageLogo)
class LogoAdmin(admin.ModelAdmin):
    pass
