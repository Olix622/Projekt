# Generated by Django 4.2.1 on 2023-06-03 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 14, 17, 34, 240810, tzinfo=datetime.timezone.utc)),
        ),
    ]
