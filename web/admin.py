from django.contrib import admin
from .models import Entrenador,Sponsor, TransmisionVivo



@admin.register(TransmisionVivo)
class TransmisionVivoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario_instagram", "en_vivo")
    list_editable = ("en_vivo",)

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "disciplina", "dias", "horarios", "orden", "activo")
    list_editable = ("orden", "activo")
    list_filter = ("activo", "disciplina")
    search_fields = ("nombre", "disciplina")


from .models import Entrenador, Sponsor

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "orden", "activo", "link")
    list_editable = ("orden", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)