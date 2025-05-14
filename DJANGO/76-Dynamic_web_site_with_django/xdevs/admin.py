from django.contrib import admin
from xdevs.models import Developer

# Register your models here.


@admin.register (Developer)
class DeveloperAdmin (admin.ModelAdmin):
    pass

