from django.db import models
from django.utils.text import slugify

class Noticia (models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(
      max_length=220,
      unique=True,
      blank=True,
      help_text="Identificador único para la URL. Se autogenera si se deja vacío.",
    )
    contenido= models.TextField()
    imagen= models.ImageField(upload_to="noticias/")
    fecha_publicacion= models.DateField(auto_now_add=True)
    publicada = models.BooleanField(default=True)
    destacada = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
     if not self.slug:
        # Genera el slug base desde el título
        base_slug = slugify(self.titulo)
        slug = base_slug
        contador = 1
        # Evita duplicados si dos noticias tienen exactamente el mismo título
        while Noticia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{contador}"
            contador += 1
        self.slug = slug
     super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo