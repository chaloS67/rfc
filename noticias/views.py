from django.shortcuts import render , get_object_or_404
from .models import Noticia

from .models import Noticia

def lista_noticias(request):
    noticias_queryset = (
        Noticia.objects
        .filter(publicada=True)
        .order_by("-fecha_publicacion")
    )
    
    # La más reciente va como destacada; las restantes van a la grilla
    destacada = noticias_queryset.first()
    noticias_resto = noticias_queryset[1:] if destacada else []

    return render(
        request,
        "noticias/lista_noticias.html",
        {
            "destacada": destacada,
            "noticias": noticias_resto,
        }
    )

def detalle_noticia(request,pk):
    noticia = get_object_or_404(Noticia, pk=pk, publicada=True)
    return render(
        request,
        "noticias/detalle_noticia.html",
        {"noticia": noticia}
    )