from django.db import models

from django.db import models

class TransmisionVivo(models.Model):
    titulo = models.CharField(
        max_length=150, 
        default="Peleas en Vivo", 
        help_text="Ej: Torneo Rawson Fight Club - En vivo"
    )
    usuario_instagram = models.CharField(
        max_length=100, 
        default="rawsonfightclub",
        help_text="Usuario de IG sin @ (ej: rawsonfightclub o el perfil de quien esté grabando)"
    )
    en_vivo = models.BooleanField(
        default=False, 
        help_text="Tildar para activar el botón en la web. Destildar al terminar."
    )

    class Meta:
        verbose_name = "Transmisión en Vivo"
        verbose_name_plural = "Transmisiones en Vivo"

    def get_url_instagram(self):
        usuario_limpio = self.usuario_instagram.strip().replace("@", "")
        return f"https://www.instagram.com/{usuario_limpio}/"

    def __str__(self):
        estado = "🔴 EN VIVO" if self.en_vivo else "Inactivo"
        return f"{self.titulo} - @{self.usuario_instagram} ({estado})"

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

class Sponsor(models.Model):
    nombre= models.CharField(max_length=120)
    logo = models.ImageField(upload_to="sponsor/",help_text='Logo del sponsor(PNG/SVG) recomendado')
    link = models.URLField(blank=True, help_text='Enlace a su web,instagram o fb (opcional)')
    orden= models.PositiveIntegerField(default=0,help_text="0 aparece primero,1 despues etc... ")
    activo= models.BooleanField(default=True, help_text="Marcar para que se vea en la pagina")

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        ordering = ["orden", "nombre"]

    def __str__(self):
        return self.nombre
