from django.db import models

# Create your models here.
from django.db import models

class FotoGaleria(models.Model):
    titulo = models.CharField(max_length=150, blank=True, help_text="Descripción o título opcional")
    imagen = models.ImageField(upload_to="galeria/")
    fecha = models.DateTimeField(auto_now_add=True)
    publicada = models.BooleanField(default=True, help_text="Marcar para que sea visible en la web")
    orden = models.PositiveIntegerField(default=0, help_text="0 aparece primero, luego 1, 2, etc.")

    class Meta:
        verbose_name = "Foto de Galería"
        verbose_name_plural = "Fotos de Galería"
        ordering = ["orden", "-fecha"]

    def __str__(self):
        return self.titulo if self.titulo else f"Foto #{self.id}"