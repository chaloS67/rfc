from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 

def home(request):
    return render (request, "web/home.html")

def profesores(request):
    return render(request, "web/profesores.html")

def conocenos(request):
    return render(request, "web/conocenos.html")

def contactos(request):
    return render(request, "web/contactos.html")