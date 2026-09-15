from django.contrib import admin
from .models import Socio
from .forms import SocioForm


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm