from django.db import models
from tinymce import models as tinymce_model


class Blog(models.Model):
  username = models.CharField(max_length=100)
  department = models.CharField(max_length=100)
  language = models.CharField(max_length=100)
  # content = models.TextField(blank=True, null=True)
  content = tinymce_model.HTMLField(null=True, blank=True)
