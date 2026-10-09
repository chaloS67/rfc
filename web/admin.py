from django.contrib import admin
from .models import Entrenador

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "disciplina", "dias", "horarios", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo", "disciplina")
    search_fields = ("nombre", "disciplina")