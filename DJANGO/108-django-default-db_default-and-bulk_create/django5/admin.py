from django.contrib import admin

# Register your models here.

from django5.models import random_names


@admin.register(random_names)
class NamesAdmin (admin.ModelAdmin):
    list_display = [
        "Name",
        "Surname",
        "age",
        "created_at",
    ]

