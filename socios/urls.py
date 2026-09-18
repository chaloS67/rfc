from django.urls import path
from .views import registrar_socio,socio_exitoso,primer_pago

urlpatterns = [

    path("registro/", registrar_socio, name = "registrar_socio"),
    path("exitoso/", socio_exitoso, name= "exitoso"),
    path("primer_pago/<int:socio_id>", primer_pago, name="primer_pago")
   
]