from django.urls import path
from .views import home,profesores,conocenos,contactos

urlpatterns = [

    path("", home, name = "home"),
    path("profesores/", profesores, name = "profesores" ),
    path("conocenos/",conocenos, name= "conocenos"),
    path("contactos/", contactos, name="contactos")
   
]