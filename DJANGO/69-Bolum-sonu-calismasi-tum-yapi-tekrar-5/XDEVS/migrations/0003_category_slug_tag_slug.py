# Generated by Django 5.1.6 on 2025-02-15 19:27

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('XDEVS', '0002_category_tag_user_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
    ]
