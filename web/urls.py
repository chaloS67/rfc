from django.urls import path
from .views import home,historia,sponsors

urlpatterns = [

    path("", home, name = "home"),
    
    path("historia/",historia, name= "historia"),
    
    path("sponsors/",sponsors, name="sponsors")
]