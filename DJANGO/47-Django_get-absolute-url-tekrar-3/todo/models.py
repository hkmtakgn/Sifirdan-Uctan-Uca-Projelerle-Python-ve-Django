from django.db import models
from django.urls import reverse

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__ (self):
        return self.title
    
    def get_absolute_url (self):
        return reverse (
            "todo_detail",
            kwargs={
                "id":self.pk
            }
        )
    
    