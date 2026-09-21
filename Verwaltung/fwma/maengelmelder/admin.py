from django.contrib import admin
from .models import Fahrzeuge, Geraete, Mangel

# Register your models here.

class FahrzeugeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class GeraeteAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class MangelAdmin(admin.ModelAdmin):
    list_display = ("kurzbeschreibung", "fahrzeug", "geraet", "erstellt_am")
    list_filter = ("fahrzeug", "geraet")
    search_fields = (
        "kurzbeschreibung",
        "mangelbeschreibung",
        "fahrzeug__name",
        "geraet__name",
    )


admin.site.register(Fahrzeuge)
admin.site.register(Geraete)
admin.site.register(Mangel)