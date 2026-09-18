from django.contrib import admin
from .models import Socio,Pagos
from .forms import SocioForm


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm


@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = (
        "socio",
        "estado",
        "fecha_envio",
    )

    list_filter = (
        "estado",
    )

    search_fields = (
        "socio__nombre",
        "socio__apellido",
        "socio__dni",
    )