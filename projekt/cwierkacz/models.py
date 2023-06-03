from django.db import models
from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField
)


class Profil(Model):
    login = CharField(max_length=128)
    haslo = CharField(max_length=128)
    imie = CharField(max_length=128)
    nazwisko = CharField(max_length=128)
    miejsce_zamieszkania = CharField(max_length=128)
    opis = TextField()