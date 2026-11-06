from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
  list_display = ("titulo", "fecha_publicacion", "publicada")
  list_editable = ("publicada",)
  list_filter = ("publicada", "fecha_publicacion")
  search_fields = ("titulo", "contenido")
  prepopulated_fields = {"slug": ("titulo",)}  # <- Se autocompleta al escribir el título