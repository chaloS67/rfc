from django.shortcuts import render,redirect
from .forms import SocioForm

# Create your views here.
def registrar_socio(request):

    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            print("SOCIO GUARDADO")
            return redirect("socio_exitoso")
        else:
            print(form.errors)
            

    else:

        form = SocioForm()
    return render (request, "socios/registro.html",{"form":form})

def socio_exitoso(request):
    return render(request,"socios/exitoso.html")