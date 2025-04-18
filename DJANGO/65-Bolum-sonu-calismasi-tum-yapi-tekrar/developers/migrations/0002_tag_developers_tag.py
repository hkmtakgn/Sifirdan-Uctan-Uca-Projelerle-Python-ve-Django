# Generated by Django 5.1.5 on 2025-01-29 19:20

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='developers',
            name='tag',
            field=models.ManyToManyField(to='developers.tag'),
        ),
    ]
