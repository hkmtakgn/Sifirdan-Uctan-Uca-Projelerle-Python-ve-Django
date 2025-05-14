from django.db import models
from autoslug import AutoSlugField

# Create your models here.



class Category (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from='title')
    is_active = models.BooleanField (default=False)

    def __str__(self):
        return self.title
    

class Tag (models.Model):
    title = models.CharField (max_length=200)
    category = models.ForeignKey (Category,blank=True,null=True,on_delete=models.SET_NULL)
    slug = AutoSlugField (populate_from='title',unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title
    

class Developer (models.Model):
    title = models.CharField (max_length=200)
    category = models.ForeignKey (Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='developer')
    tag = models.ManyToManyField (Tag,blank=True,null=True)
    content = models.TextField (blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title
    
