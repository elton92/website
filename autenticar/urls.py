from django.urls import path

from .views import *

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('login/', acceder, name="login"),
    path('sair/', sair, name="sair"),
]
