from django.db import models
from django.shortcuts import reverse
# Create your models here.
from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Kategori (models.Model):
    title = models.CharField (max_length=200)
    slug = AutoSlugField (populate_from="title",unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse (
            "app2:kategori",
            kwargs={
                "kategori_slug":self.slug,
            }
        )



class Etiket (models.Model):
    title = models.CharField (max_length=200)
    kategori = models.ForeignKey (Kategori,on_delete=models.SET_NULL,null=True,blank=True)
    slug = AutoSlugField (populate_from="title",unique=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse (
            "app2:tag_set",
            kwargs={
                "kategori_slug":self.kategori.slug,
                "tag_slug":self.slug,

            }
        )

class Gelistirici (models.Model):
    title = models.CharField (max_length=200)
    etiket = models.ManyToManyField (Etiket)
    content = models.TextField (blank=True,null=True)
    is_active = models.BooleanField (default=False)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse (
            "app2:gelistirici",
            kwargs={
                "kategori_slug":self.etiket.first().kategori.slug,
                "id":self.pk,
            }
        )

        