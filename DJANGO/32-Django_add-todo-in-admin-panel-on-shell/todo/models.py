from django.db import models

# Create your models here.

class Todo (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=False)
