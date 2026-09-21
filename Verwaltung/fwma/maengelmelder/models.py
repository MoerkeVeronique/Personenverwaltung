from django.db import models

# Create your models here.

class Fahrzeuge(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Fahrzeuge"

    def __str__(self):
        return self.name


class Geraete(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Geräte"

    def __str__(self):
        return self.name


class Mangel(models.Model):
    kurzbeschreibung = models.TextField("Kurzbeschreibung (Freitext)")
    mangelbeschreibung = models.TextField("Mangelbeschreibung (Freitext)")

    fahrzeug = models.ForeignKey(
        Fahrzeuge,
        on_delete=models.PROTECT,
        verbose_name="Fahrzeug",
    )

    geraet = models.ForeignKey(
        Geraete,
        on_delete=models.PROTECT,
        verbose_name="Gerät",
    )

    erstellt_am = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mangel"
        verbose_name_plural = "Mängel"

    def __str__(self):
        return f"{self.kurzbeschreibung[:30]} ({self.erstellt_am})"