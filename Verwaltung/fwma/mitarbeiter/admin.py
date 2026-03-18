from django.contrib import admin
from django import forms
from .models import Mitarbeiter, MedizinischeDaten, Notfallkontakt
# Register your models here.


class NotfallkontaktForm(forms.ModelForm):
    class Meta:
        model = Notfallkontakt
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.beziehung != 'andere':
            self.fields['beziehung_andere'].widget = forms.HiddenInput()

class NotfallkontaktInline(admin.StackedInline):
    model = Notfallkontakt
    form = NotfallkontaktForm
    extra = 1
    max_num = 1


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
