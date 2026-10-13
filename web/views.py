from django.shortcuts import render
from noticias.models import Noticia
from galeria.models import FotoGaleria
from .models import Entrenador,Sponsor,TransmisionVivo


def home(request):

    # Buscamos la última noticia publicada
    ultima_noticia = (
        Noticia.objects
        .filter(publicada=True)
        .order_by("-fecha_publicacion")
        .first()
    )

    en_vivo = TransmisionVivo.objects.filter(en_vivo = True).first()


    # Slides normales del carrusel Por ahroa estaticos
    slides_home = [
        {
            "fondo": "homecarrusel1.png",
            "overlay": "textobanda.svg",
        },
        {
            "fondo": "homecarrusel2.png",
            "overlay": "textocomunidad.svg",
        },
        {
            "fondo": "homecarrusel3.png",
            "overlay": "textofamilia.svg",
        },
    ]

    # Si existe una noticia publicada,
    # la agregamos como una slide más
    if ultima_noticia:
        slides_home.append({
            "es_noticia": True,
            "fondo_noticia": ultima_noticia.imagen,
            "titulo_noticia": ultima_noticia.titulo,
            "slug_noticia": ultima_noticia.slug,
            "id_noticia" : ultima_noticia.id,
            
        })

    # Galería dinámica
    fotos_galeria = FotoGaleria.objects.filter(publicada=True).order_by("orden", "-fecha")

    # Entrenadores desde la base de datos
    entrenadores = Entrenador.objects.filter(activo=True).order_by("orden")

    # Sponsors dinámicos de la base de datos
    sponsors = Sponsor.objects.filter(activo=True).order_by("orden")
    
    return render(
        request,
        "web/home.html",
        {
            "entrenadores": entrenadores,
            "fotos_galeria": fotos_galeria,
            "sponsors": sponsors,
            "slides_home": slides_home,
            "en_vivo":en_vivo
        }
    )

def historia(request):
    return render(request, "web/historia.html")

def sponsors(request):
    sponsors_list = Sponsor.objects.filter(activo=True).order_by("orden")
    return render(
        request,
        "web/sponsors.html",
        {
            "sponsors": sponsors_list
        }
    )
 
