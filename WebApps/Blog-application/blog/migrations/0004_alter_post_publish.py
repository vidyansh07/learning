# Generated by Django 4.1.13 on 2024-03-02 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 2, 4, 53, 57, 662517, tzinfo=datetime.timezone.utc)),
        ),
    ]
