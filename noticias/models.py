from django.db import models

class Noticia (models.Model):
    titulo = models.CharField(max_length=100)
    contenido= models.TextField()
    imagen= models.ImageField(upload_to="noticias/")
    fecha_publicacion= models.DateField(auto_now_add=True)
    publicada = models.BooleanField(default=True)
    

    def __str__(self):
        return self.titulo