# Generated by Django 5.1.4 on 2024-12-14 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]