from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 

def home(request):
    return render (request, "web/home.html")

def profesores(request):
    return render(request, "web/profesores.html")

def conocenos(request):
    return render(request, "web/conocenos.html")

def galeria(request):
    return render(request, "web/galeria.html")

def profesores(request):

    profesores = [
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
        "proboste.jpeg"

    ]
    return render(request, "web/profesores.html",{"profesores": profesores}) 

def galeria(request):    

    fotos = [
        "img1.jpeg",
        "img2.jpeg",
        "img3.jpeg",
        "img4.jpeg",
        "img5.jpeg"
        
    ]
    return render(request, "web/galeria.html",{"fotos": fotos}) 

