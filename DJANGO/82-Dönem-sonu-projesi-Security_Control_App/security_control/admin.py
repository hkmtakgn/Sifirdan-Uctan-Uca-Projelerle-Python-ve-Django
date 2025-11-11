from django.contrib import admin
from security_control.models import Visitor, Subcontractor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "company",
        "email",
        "phone_number",
    )


@admin.register(Subcontractor)
class SubcontractorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "company",
        "email",
        "phone_number",
    )
