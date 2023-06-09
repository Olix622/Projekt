# Generated by Django 4.2.1 on 2023-06-15 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0025_profil_user_alter_post_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='haslo',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='imie',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='miejsce_zamieszkania',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='nazwa_uzytkownika',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='nazwisko',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='opis',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 16, 52, 27, 583652, tzinfo=datetime.timezone.utc)),
        ),
    ]
