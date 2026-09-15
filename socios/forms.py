from django import forms
from django.utils import timezone
from .models import Socio


class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        fields = [
            "nombre",
            "apellido",
            "dni",
            "fecha_nac",
            "telefono",
            "email",
            "responsable",
            "telefono_responsable",
        ]

        widgets = {
            "fecha_nac": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d"
            )
        }

    def clean(self):
        cleaned_data = super().clean()

        fecha_nac = cleaned_data.get("fecha_nac")
        responsable = cleaned_data.get("responsable")
        telefono_responsable = cleaned_data.get("telefono_responsable")

        if fecha_nac:
            hoy = timezone.localdate()

            edad = hoy.year - fecha_nac.year

            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1

            if edad < 18:

                if not responsable:
                    self.add_error(
                        "responsable",
                        "Debe indicar un responsable si es menor de edad."
                    )

                if not telefono_responsable:
                    self.add_error(
                        "telefono_responsable",
                        "Debe indicar el teléfono del responsable."
                    )

        return cleaned_data