from django.shortcuts import render


SPONSORS = [

        {
            "nombre":"Team Agüero",
            "logo":"teamaguero.png",
            "link":"https://instagram.com/af_team_aguero"
        },

        {
            "nombre":"Deporte Capital",
            "logo":"deportecapital.png",
            "link":"https://instagram.com/"
        },

        {
            "nombre":"Colombia Barber Shop",
            "logo":"colombia.png",
            "link":"https://instagram.com/"
        },

        {
            "nombre":"Monkey",
            "logo":"monkey.png",
            "link":"https://instagram.com/"
        }

]


def home(request):
    return render(request, "web/home.html",{"sponsors" : SPONSORS})


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
 
