from django.contrib import admin
from .models import FotoGaleria

# Register your models here.
@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "publicada", "orden", "fecha")
    list_editable = ("publicada", "orden")
    list_filter = ("publicada", "fecha")
    search_fields = ("titulo",)