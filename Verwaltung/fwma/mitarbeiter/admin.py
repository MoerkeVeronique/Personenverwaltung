from django.contrib import admin
from django import forms
from .models import Mitarbeiter, MedizinischeDaten, Notfallkontakt, Qualifikation, MitarbeiterQualifikation, PrivateDaten
# Register your models here.

class QualifikationInline(admin.TabularInline):
    model = MitarbeiterQualifikation
    extra = 1

class PrivateDatenInline(admin.StackedInline):
    model = PrivateDaten
    extra = 1
    max_num = 1

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

class MedizinischeDatenInline(admin.StackedInline):
    model = MedizinischeDaten
    extra = 1
    max_num = 1


class MitarbeiterAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Mitarbeiter"
        model = Mitarbeiter
    list_display = ('vorname', 'nachname', 'email', 'telefonnummer')
    search_fields = ('vorname', 'nachname', 'email')
    inlines = [NotfallkontaktInline, PrivateDatenInline, MedizinischeDatenInline, QualifikationInline]

class MedizinischeDatenAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Medizinische Daten"
        model = MedizinischeDaten
    list_display = ('mitarbeiter', 'blutgruppe', 'allergien', 'chronische_erkrankungen')
    search_fields = ('mitarbeiter__vorname', 'mitarbeiter__nachname', 'blutgruppe')

class QualifikationAdmin(admin.ModelAdmin):
    search_fields = ['name']  
    list_display = ['name']

class PrivateDatenAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Private Daten"
        model = PrivateDaten
    list_display = ('mitarbeiter', 'adresse', 'geburtsdatum')
    search_fields = ('mitarbeiter__vorname', 'mitarbeiter__nachname', 'adresse')


admin.site.register(Qualifikation)  
admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(MedizinischeDaten, MedizinischeDatenAdmin)
admin.site.register(PrivateDaten, PrivateDatenAdmin)