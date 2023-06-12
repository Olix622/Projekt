from django.db import models
from django.db.models import Model, CharField, TextField
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    objects = None
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Profil(Model):
    nazwa_uzytkownika = CharField(max_length=128)
    haslo = CharField(max_length=128)
    imie = CharField(max_length=128)
    nazwisko = CharField(max_length=128)
    miejsce_zamieszkania = CharField(max_length=128)
    opis = TextField()
