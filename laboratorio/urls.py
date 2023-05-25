from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    path('inicio/', views.inicio, name='inicio.html'),
    path('producto/', views.producto, name='producto.html'),
    path('producto/altaProducto/', views.altaProducto, name='altaProducto.html'),
]