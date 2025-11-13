from django.db import models

# Create your models here.

import random
from django.db.models.functions import Now

def age_generator ():
    return random.randint(1,100)

class random_names (models.Model):
    Name = models.CharField (max_length=100)
    Surname = models.CharField (max_length=100)
    age = models.SmallIntegerField (default=age_generator)
    created_at = models.DateTimeField(db_default=Now())

    def __str__ (self):
        return self.Name + " " + self.Surname
    
