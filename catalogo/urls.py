from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('plantas/', views.lista_plantas, name='lista_plantas'),
]