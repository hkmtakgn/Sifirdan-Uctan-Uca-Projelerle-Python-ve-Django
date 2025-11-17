from django.contrib import admin

# Register your models here.

from djangopractices.models import SquareCalc


@admin.register (SquareCalc)
class SquareCalcAdmin (admin.ModelAdmin):

    list_display = [
        "area",
    ]

