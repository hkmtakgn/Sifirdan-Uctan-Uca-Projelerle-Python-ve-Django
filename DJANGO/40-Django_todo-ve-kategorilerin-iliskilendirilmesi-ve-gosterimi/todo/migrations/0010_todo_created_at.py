# Generated by Django 5.1.4 on 2024-12-22 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_todo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]