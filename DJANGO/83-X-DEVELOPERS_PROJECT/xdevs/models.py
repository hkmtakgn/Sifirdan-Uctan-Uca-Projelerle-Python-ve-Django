from django.db import models
from autoslug import AutoSlugField


class W_Languages(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  slug = AutoSlugField(populate_from="title", unique=True)
  is_active = models.BooleanField(default=False)

  def __str__(self):
    return self.title


class Web_Pages(models.Model):
  title = models.CharField(max_length=100)
  tag = models.ManyToManyField(W_Languages)
  slug = AutoSlugField(populate_from="title", unique=True)
  is_active = models.BooleanField(default=False)

  def __str__(self):
    return self.title


class Developer(models.Model):
  title = models.CharField(max_length=100)
  tag = models.ManyToManyField(W_Languages, related_name="developer")
  content = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=False)

  def __str__(self):
    return self.title
