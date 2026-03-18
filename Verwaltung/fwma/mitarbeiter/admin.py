from django.contrib import admin
from .models import Mitarbeiter, MedizinischeDaten, Notfallkontakt
# Register your models here.


class NotfallkontaktInline(admin.StackedInline):
    model = Notfallkontakt
    extra = 1  #zeigt ein leeres Formular beim Anlegen
    max_num = 1  #nur ein Notfallkontakt pro Mitarbeiter

class MitarbeiterAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Mitarbeiter"
        model = Mitarbeiter
    list_display = ('vorname', 'nachname', 'email', 'telefonnummer')
    search_fields = ('vorname', 'nachname', 'email')
    inlines = [NotfallkontaktInline]

class MedizinischeDatenAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Medizinische Daten"
        model = MedizinischeDaten
    list_display = ('mitarbeiter', 'blutgruppe', 'allergien', 'chronische_erkrankungen')
    search_fields = ('mitarbeiter__vorname', 'mitarbeiter__nachname', 'blutgruppe')




admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(MedizinischeDaten, MedizinischeDatenAdmin)
