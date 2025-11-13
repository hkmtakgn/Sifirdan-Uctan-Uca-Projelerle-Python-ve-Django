1- 

from django.db import models

# Create your models here.

import random


def age_generator ():
    return random.randint(1,100)

class random_names (models.Model):
    Name = models.CharField (max_length=100)
    Surname = models.CharField (max_length=100)
    age = models.SmallIntegerField (default=age_generator) #hesaplamayı python tarafından yapar sonra veritabanına gönderir.

    def __str__ (self):
        return self.Name + " " + self.Surname
    
2-

from django.contrib import admin

# Register your models here.

from django5.models import random_names


@admin.register(random_names)
class NamesAdmin (admin.ModelAdmin):
    list_display = [
        "Name",
        "Surname",
        "age",
    ]

    

3-

from django5.models import random_names

list = [random_names(Name=f"User {i}",Surname=f"Usersurname {i}") for i in range(1,100)]


random_names.objects.bulk_create(list)

4-

from django.db.models.functions import Now

created_at = models.DateTimeField(db_default=Now()) #Verileri oluşturup gönderir db_default ile de hesaplamayı veritabanında yapıp işler. Bu işlem daha hızlı ve güvenilirdir.




