from django.contrib import admin

# Register your models here.

from pages.models import register_model,blog_post

@admin.register (register_model)
class RegisterAdmin (admin.ModelAdmin):
    list_display = ("username","email","dept")


@admin.register (blog_post)
class BlogPostAdmin (admin.ModelAdmin):
    list_display = [
        "username",
    ]
