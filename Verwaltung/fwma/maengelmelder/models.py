from django.db import models

# Create your models here.
class Kurzbeschreibung(models.Model):
    beschreibung = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Kurzbeschreibungen"

    def __str__(self):
        return self.beschreibung

class Fahrzeuge(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Fahrzeuge"

    def __str__(self):
        return self.name

class Geraete(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Geräte"

    def __str__(self):
        return self.name

class Mangelbeschreibung(models.Model):
    beschreibung = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Mangelbeschreibungen"

    def __str__(self):
        return self.beschreibung

