from django.shortcuts import render
from .models import Noticia

def lista_noticias(request): 

    noticias= Noticia.objects.filter(publicada=True).order_by("-fecha_publicacion")

    return render (request,"noticias/lista_noticias.html",{"noticias": noticias})
