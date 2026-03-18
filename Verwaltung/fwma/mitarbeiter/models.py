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
    BEZIEHUNGEN = [
        ('elternteil', 'Elternteil'),
        ('ehepartner', 'Ehepartner/in'),
        ('kind', 'Kind'),
        ('geschwister', 'Geschwister'),
        ('freund', 'Freund/in'),
        ('andere', 'Andere'),
    ]
    
    mitarbeiter = models.OneToOneField(Mitarbeiter, on_delete=models.CASCADE, related_name='notfallkontakt')
    name = models.CharField(max_length=100)
    beziehung = models.CharField(max_length=20, choices=BEZIEHUNGEN, default='andere')
    beziehung_andere = models.CharField(max_length=100, blank=True, help_text="Nur bei 'Andere' ausfüllen")
    handynummer = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.get_beziehung_display()})"
