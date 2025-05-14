from django.db import models

# Create your models here.

class Todo (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_information = models.CharField(max_length=200)
    from_company = models.CharField(max_length=200)
    to_company = models.CharField(max_length=200)
    who_visit = models.CharField(max_length=200)
    enter_date = models.CharField(max_length=200)
    enter_clock = models.CharField(max_length=200)
    exit_date = models.CharField(max_length=200)
    exit_clock = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=False)

