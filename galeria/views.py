from django.shortcuts import render


from galeria.models import FotoGaleria


def home(request):
    # Traemos las fotos publicadas y ordenadas
    fotos_galeria = FotoGaleria.objects.filter(publicada=True)

    # ... tu lógica existente de slides_home y noticias ...

    context = {
        "slides_home": slides_home,
        "fotos_galeria": fotos_galeria,
        # ... resto del contexto ...
    }
    return render(request, "web/home.html", context)