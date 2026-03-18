from django.contrib import admin
from .models import Mitarbeiter, MedizinischeDaten
# Register your models here.


class MitarbeiterAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Mitarbeiter"
        model = Mitarbeiter
    list_display = ('vorname', 'nachname', 'email', 'telefonnummer')
    search_fields = ('vorname', 'nachname', 'email')

class MedizinischeDatenAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Medizinische Daten"
        model = MedizinischeDaten
    list_display = ('mitarbeiter', 'blutgruppe', 'allergien', 'chronische_erkrankungen')
    search_fields = ('mitarbeiter__vorname', 'mitarbeiter__nachname', 'blutgruppe')

admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(MedizinischeDaten, MedizinischeDatenAdmin)