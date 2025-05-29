from django.db import models

# Create your models here.


class Visitor(models.Model):
  full_name = models.CharField(max_length=255)
  company = models.CharField(max_length=255)
  email = models.EmailField()
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  date_of_entry = models.CharField(max_length=255)
  time_of_entry = models.CharField(max_length=255)
  meeting_with = models.CharField(max_length=255)
  purpose_of_visit = models.TextField()
  rules_form = models.ImageField(upload_to='rules_form/',
                                 blank=True,
                                 null=True)

  def __str__(self):
    return self.full_name


class Subcontractor(models.Model):
  full_name = models.CharField(max_length=255)
  company = models.CharField(max_length=255)
  email = models.EmailField()
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  date_of_entry = models.CharField(max_length=255)
  time_of_entry = models.CharField(max_length=255)
  purpose_of_visit = models.TextField()
  rules_form = models.ImageField(upload_to='substractor-rules-form/',
                                 blank=True,
                                 null=True)

  def __str__(self):
    return self.full_name
