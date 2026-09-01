from django.shortcuts import render


SPONSORS = [

        {
            "nombre":"morpho",
            "logo":"morpho.png",
            "link":"#"
        },

        {
            "nombre":"Red textil",
            "logo":"redtextil.svg",
            "link":"#"
        },

        {
            "nombre":"Monkey",
            "logo":"monkeyS.svg",
            "link":"#"
        },

        {
            "nombre":"Travesuras",
            "logo":"travesuras.svg",
             "link":"#"
        },

        {
            "nombre":"ingenio",
            "logo":"ingenio.png",
            "link":"#"
        },

        {
            "nombre":"Sugar",
            "logo":"sugar.svg",
            "link":"#"
        }

]

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

def home(request):

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
 
