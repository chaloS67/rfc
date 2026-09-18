from django.shortcuts import render,redirect,get_object_or_404
from .forms import SocioForm,PagosForm
from .models import Socio,Pagos

# Create your views here.
def registrar_socio(request):

    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            return redirect("primer_pago",socio_id=socio.id)
        else:
            print(form.errors)
            

    else:

        form = SocioForm()
    return render (request, "socios/registro.html",{"form":form})

def socio_exitoso(request):
    return render(request,"socios/exitoso.html")


def primer_pago(request,socio_id):
    socio = get_object_or_404(Socio,id = socio_id)

    if request.method == "POST":
        form= PagosForm(request.POST, request.FILES)

        if form.is_valid():

            pago = form.save(commit=False)

            pago.socio = socio  

            pago.save()

            return redirect("exitoso")
        
    else:
        form = PagosForm()
    return render (
        request,
        "socios/primer_pago.html",
        {
            "form":form,
            "socio":socio
        }
    )