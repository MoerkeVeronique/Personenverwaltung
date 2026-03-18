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


class MedizinischeDaten(models.Model):
    mitarbeiter = models.OneToOneField(Mitarbeiter, on_delete=models.CASCADE, related_name='medizinische_daten')
    blutgruppe = models.CharField(max_length=3)
    allergien = models.TextField(blank=True)
    chronische_erkrankungen = models.TextField(blank=True)
    medikamende = models.TextField(blank=True)

    def __str__(self):
        return f"Medizinische Daten von {self.mitarbeiter.vorname} {self.mitarbeiter.nachname}"


class Notfallkontakt(models.Model):
    mitarbeiter = models.OneToOneField(Mitarbeiter, on_delete=models.CASCADE, related_name='notfallkontakt')
    name = models.CharField(max_length=100)
    beziehung = models.CharField(max_length=50)
    handynummer = models.CharField(max_length=20)

    def __str__(self):
        return f"Notfallkontakt von {self.mitarbeiter.vorname} {self.mitarbeiter.nachname}: {self.name} ({self.beziehung})"