# Generated by Django 4.2.1 on 2023-06-03 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0013_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 15, 6, 26, 869227, tzinfo=datetime.timezone.utc)),
        ),
    ]
