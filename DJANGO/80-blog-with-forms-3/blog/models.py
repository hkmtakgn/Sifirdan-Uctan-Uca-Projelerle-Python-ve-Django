from django.db import models
from tinymce import models as tinymceModels

# Create your models here.


class post_model(models.Model):
  title = models.CharField(max_length=100)
  content = tinymceModels.HTMLField()
  img = models.ImageField(upload_to="img/")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
