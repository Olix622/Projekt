# Generated by Django 4.2.1 on 2023-06-15 17:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posty', '0027_alter_post_published_delete_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 17, 3, 51, 85693, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_uzytkownika', models.CharField(max_length=128)),
                ('haslo', models.CharField(max_length=128)),
                ('imie', models.CharField(max_length=128)),
                ('nazwisko', models.CharField(max_length=128)),
                ('miejsce_zamieszkania', models.CharField(max_length=128)),
                ('opis', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]