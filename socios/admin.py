from django.contrib import admin
from .models import Socio,Pagos
from django.utils.html import format_html 
from .forms import SocioForm


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):

    form = SocioForm
    list_display = [
            "nombre",
            "estado",
            "numero_socio"
        ]   

    list_filter = (
            "estado",
            
        )


@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = (
        "socio",
        "estado",
        "fecha_envio",
        "ver_comprobante"
    )

    list_filter = (
        "estado",
        
    )

    search_fields = (
        "socio__nombre",
        "socio__apellido",
        "socio__dni",
    )

    # Función para generar el enlace clickeable al comprobante
    def ver_comprobante(self, obj):
        if obj.comprobante:
            return format_html('<a href="{}" target="_blank" style="color: #e9521d;"><b>Ver Archivo</b></a>', obj.comprobante.url)
        return "Sin archivo"
    
    ver_comprobante.short_description = "Comprobante"