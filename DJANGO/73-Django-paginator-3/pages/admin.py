from django.contrib import admin
from pages.models import Page,Developer

# Register your models here.

@admin.register (Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register (Developer)
class DevAdmin (admin.ModelAdmin):
    pass

