from django.urls import path
from .views import home,profesores,conocenos,galeria

urlpatterns = [

    path("", home, name = "home"),
    path("profesores/", profesores, name = "profesores" ),
    path("conocenos/",conocenos, name= "conocenos"),
    path("galeria/", galeria, name="galeria")
]