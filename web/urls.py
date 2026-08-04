from django.urls import path
from .views import home,actividades,historia,galeria,sponsors

urlpatterns = [

    path("", home, name = "home"),
    path("actividades/",actividades, name = "profesores" ),
    path("historia/",historia, name= "historia"),
    path("galeria/",galeria, name="galeria"),
    path("sponsors/",sponsors, name="sponsors")
]