from django.db import models

# Create your models here.


class Mitarbeiter(models.Model):
    id = models.AutoField(primary_key=True)
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefonnummer = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.vorname} {self.nachname}"


