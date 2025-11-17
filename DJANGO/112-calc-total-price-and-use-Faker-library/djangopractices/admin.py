from django.contrib import admin

# Register your models here.

from djangopractices.models import SquareCalc , Product


@admin.register (SquareCalc)
class SquareCalcAdmin (admin.ModelAdmin):

    list_display = [
        "area",
    ]

@admin.register (Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = [
        "title",
        "company",
        "total_price",
    ]

