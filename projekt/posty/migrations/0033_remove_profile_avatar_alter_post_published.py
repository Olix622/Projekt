# Generated by Django 4.2.1 on 2023-06-17 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0032_alter_post_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 9, 8, 32, 964329, tzinfo=datetime.timezone.utc)),
        ),
    ]
