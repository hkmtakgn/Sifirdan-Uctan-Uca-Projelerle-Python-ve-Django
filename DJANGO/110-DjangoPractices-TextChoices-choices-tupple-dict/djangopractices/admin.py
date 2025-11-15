from django.contrib import admin

from djangopractices.models import anon_user


@admin.register(anon_user)
class AnonAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "surname",
        "hobbies",
        "skills",
        "data_base",
        "created_at",
    ]
