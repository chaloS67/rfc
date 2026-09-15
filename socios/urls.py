from django.urls import path
from .views import registrar_socio,socio_exitoso

urlpatterns = [

    path("registro/", registrar_socio, name = "registrar_socio"),
    path("exitoso/", socio_exitoso, name= "socio_exitoso"),
   
]