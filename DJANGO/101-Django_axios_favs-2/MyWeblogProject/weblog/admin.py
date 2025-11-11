from django.contrib import admin
from weblog.models import Page, Interface_user, Post, FavPost

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'page_slug',
        'is_active',
    ]


admin.site.register(Page, PageAdmin)


@admin.register(Interface_user)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "nickname",
        "first_name",
        "last_name",
        "is_active",
        "is_online",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "slug",
        "is_active",
    ]


@admin.register(FavPost)
class FavPostAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "id", "is_active", "created_at"]
