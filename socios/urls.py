from django.urls import path
from .views import registrar_socio,socio_exitoso,primer_pago
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("registro/", registrar_socio, name = "registrar_socio"),
    path("exitoso/", socio_exitoso, name= "exitoso"),
    path("primer_pago/<int:socio_id>", primer_pago, name="primer_pago"),
    path('login/', auth_views.LoginView.as_view(template_name='socios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
