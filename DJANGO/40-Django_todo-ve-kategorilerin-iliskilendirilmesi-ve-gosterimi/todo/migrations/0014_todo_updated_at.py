# Generated by Django 5.1.4 on 2024-12-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_alter_todo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
