from django.contrib import admin
from .models import Entrenador,Sponsor, TransmisionVivo,HorarioEntrenador




@admin.register(TransmisionVivo)
class TransmisionVivoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario_instagram", "en_vivo")
    list_editable = ("en_vivo",)


class HorarioEntrenadorInline(admin.TabularInline):
    model = HorarioEntrenador
    extra = 1  # Muestra 1 fila vacía lista para cargar una disciplina y horario

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    inlines = [HorarioEntrenadorInline]
    # Solo dejamos los campos que realmente siguen adentro del modelo Entrenador
    list_display = ("nombre", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "orden", "activo", "link")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)