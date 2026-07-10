from django.urls import path
from .views import home,profesores,historia,galeria

urlpatterns = [

    path("", home, name = "home"),
    path("profesores/", profesores, name = "profesores" ),
    path("historia/",historia, name= "historia"),
    path("galeria/", galeria, name="galeria")
]