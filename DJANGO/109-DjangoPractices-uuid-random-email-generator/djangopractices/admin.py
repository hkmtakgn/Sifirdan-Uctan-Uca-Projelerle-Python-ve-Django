from django.contrib import admin

# Register your models here.

from djangopractices.models import AnonimUser


@admin.register(AnonimUser)
class AnonimUserAdmin(admin.ModelAdmin):
    list_display = [
        "nickname",
        "email",
        "created_at",
    ]
