from django.db import models

# Create your models here.


from django.db.models import F
from faker import Faker


class SquareCalc (models.Model):
    side = models.IntegerField ()
    area = models.GeneratedField (
        expression = F ("side") * F ("side"),
        output_field = models.BigIntegerField (),
        db_persist = True,
    )


def company_generator ():
    faker = Faker ()
    list = []
    for _ in range (10):
        rand_comp = faker.company ()
        list.append (("comp",rand_comp))
    return list

def generate_count():
    return [(i,i) for i in range(11)]


class Product (models.Model):
    title = models.CharField (max_length=100)
    company = models.CharField (max_length=100,choices=company_generator)
    count = models.SmallIntegerField (choices=generate_count,db_default=0)
    price = models.DecimalField (max_digits=10,decimal_places=2)
    total_price = models.GeneratedField (
        expression=F("count")*F("price"),
        output_field = models.DecimalField (max_digits=10,decimal_places=2),
        db_persist=True,
    )

    