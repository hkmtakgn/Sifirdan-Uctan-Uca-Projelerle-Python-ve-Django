from django.contrib import admin
from blog.models import register_model,add_story_model

# Register your models here.

@admin.register (register_model)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "dept",
    ]


@admin.register (add_story_model)
class AddStoryModelAdmin (admin.ModelAdmin):
    list_display = [
        "username",
        "dept",
    ]

