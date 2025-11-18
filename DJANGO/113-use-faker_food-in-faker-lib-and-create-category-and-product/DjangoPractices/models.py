from django.db import models

from faker_food import FoodProvider
from faker import Faker

faker = Faker()
faker.add_provider(FoodProvider)

sushi_cat = [(f"{i}", faker.sushi()) for i in range(7)]

categories = [
    ("fruit_vegetables", "Fruit and vegetables"),
    ("starchy_food", "Starchy food"),
    ("dairy", "Dairy"),
    ("protein", "Protein"),
    ("fat", "Fat"),
]


class Category(models.Model):
    title = models.CharField(max_length=33,
                             choices=categories,
                             default=categories[0])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        category_exists = Category.objects.filter(title=self.title)
        if category_exists:
            print("Zaten var!")
            return
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100, choices=sushi_cat)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        prods = Product.objects.filter(title=self.title).exists()
        if prods:
            print("Zaten var!")
            return
        super().save(*args, **kwargs)
