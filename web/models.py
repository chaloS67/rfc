from django.db import models

class Entrenador (models.Model):
    nombre = models.CharField(max_length=50)
    disciplina = models.CharField()
    foto = models.ImageField(upload_to="entrenadores/")

    #Informacion adicional de clases 
    dias = models.CharField(
        max_length=150,
        blank=True,
        help_text="Ej: Lunes,Miercoles y viernes"
    )
    horarios = models.CharField(
        max_length=150,
        blank=True,
        help_text="Ej : 19:00 a 20:30"
    )

    info_adicional = models.CharField(
        max_length=200,
        blank=True,
        help_text="Ej: Todos los niveles / Mixto / Turno tarde"
    )

    orden = models.PositiveIntegerField(default=0, help_text="0 aparece primero, 1 después, etc.")
    activo = models.BooleanField(default=True, help_text="Marcar para que se vea en la web")

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = ["orden", "nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.disciplina})"
