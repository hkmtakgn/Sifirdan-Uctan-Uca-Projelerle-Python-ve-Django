from django.contrib import admin
from weblog.models import Post, Tag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "content",
        "is_active",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]
