from django.shortcuts import render
from noticias.models import Noticia



SPONSORS = [


        {
            "nombre":"Ayelenvalle",
            "logo":"ayelenvalle.svg",
            "link":"https://www.instagram.com/ayelenvalle_estetica/"
        },

        {
            "nombre":"colombia",
            "logo":"colombia.svg",
            "link":"https://www.instagram.com/colombia.bsh/"
        },

        {
            "nombre":"Deportivo capital",
            "logo":"deportivocapital.svg",
             "link":"https://www.facebook.com/profile.php?id=61580159597802"
        },

        {
            "nombre":"ingenio",
            "logo":"ingenio.svg",
            "link":"https://www.instagram.com/ingenio.ia/   "
        },

        {
            "nombre":"laflia",
            "logo":"laflia.svg",
            "link":"https://www.facebook.com/search/top?q=lavadero%20la%20flia"
        },

        {
            "nombre":"morpho",
            "logo":"morpho.svg",
            "link":"https://www.instagram.com/morp.ho3d/"
        },

        {
            "nombre":"teamaguero",
            "logo":"teamaguero.svg",
            "link":"https://www.instagram.com/af_team_aguero/"
        },

]



def home(request):

    # Buscamos la última noticia publicada
    ultima_noticia = (
        Noticia.objects
        .filter(publicada=True)
        .order_by("-fecha_publicacion")
        .first()
    )

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
            "id_noticia" : ultima_noticia.id,
            
        })
        
    entrenadores = [
        {
            
            "imagen": "abraham.png",
            "disciplina": "Kickboxing",
        },
        {
          
            "imagen": "anto.png",
            "disciplina": "MMA femenino",
        },
        {
            
            "imagen": "charly.png",
            "disciplina": "MMA / Wrestling",
        },
        {
        
            "imagen": "enzo.png",
            "disciplina": "Kickboxing",
        },
        {
        
            "imagen": "julio.png",
            "disciplina": "Kickboxing",
        },

        {
        
            "imagen": "luciano.png",
            "disciplina": "Kickboxing",
        },

        {
        
            "imagen": "marino.png",
            "disciplina": "Kickboxing",
        },

        {
        
            "imagen": "matias.png",
            "disciplina": "Kickboxing",
        },


        {
        
            "imagen": "maxi.png",
            "disciplina": "Kickboxing",
        },

        {
        
            "imagen": "omar.png",
            "disciplina": "Kickboxing",
        },

        {
        
            "imagen": "rafa.png",
            "disciplina": "Kickboxing",
        },
    ]

    fotos = [
        "img1.jpeg",
        "img2.jpeg",
        "img3.jpeg",
        "img4.jpeg",
        "img5.jpeg",
        "img6.jpeg",
    ]

    return render(
        request,
        "web/home.html",
        {
            "entrenadores": entrenadores,
            "fotos": fotos,
            "sponsors": SPONSORS,
            "slides_home": slides_home,
        }
    )


def actividades(request):
    actividades = [
        "abrham.jpeg",
        "antonella.jpeg",
        "charly.jpeg",
        "enzo.jpeg",
        "felipe.jpeg",
        "julio.jpeg",
        "marino.jpeg",
        "maxi.jpeg",
        "melisa.jpeg",
        "omar_lucha.jpeg",
        "omar_mma.jpeg",
        "proboste.jpeg",
    ]
    return render(request, "web/actividades.html", {"actividades": actividades})


def galeria(request):
    fotos = [
        "img1.jpeg",
        "img2.jpeg",
        "img3.jpeg",
        "img4.jpeg",
        "img5.jpeg",
        "img6.jpeg",
        "img7.jpeg",
    ]
    return render(request, "web/galeria.html", {"fotos": fotos})


def historia(request):
    return render(request, "web/historia.html")

def sponsors(request):

    return render(request,"web/sponsors.html",{
        "sponsors": SPONSORS
    }
)
 
