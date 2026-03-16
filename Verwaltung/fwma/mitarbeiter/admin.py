from django.contrib import admin
from .models import Mitarbeiter
# Register your models here.


class MitarbeiterAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Mitarebtier"
        model = Mitarbeiter
    list_display = ('vorname', 'nachname', 'email', 'telefonnummer')
    search_fields = ('vorname', 'nachname', 'email')


admin.site.register(Mitarbeiter, MitarbeiterAdmin)