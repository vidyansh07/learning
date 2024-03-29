# Generated by Django 5.0.1 on 2024-03-20 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_book_alter_post_publish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 13, 29, 37, 95244, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
