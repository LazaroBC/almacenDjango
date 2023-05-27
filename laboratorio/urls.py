from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    path('inicio/', views.inicio, name='inicio.html'),

    path('producto/', views.producto, name='producto.html'),
    path('altaProducto/', views.altaProducto, name='altaProducto.html'),
    path('bajaProducto/', views.bajaProducto, name='bajaProducto.html'),
    path('cambioProducto/', views.cambioProducto, name='cambioProducto.html'),
    path('listaProducto/', views.listaProducto, name='listaProducto.html'),

    path('cliente/', views.cliente, name='cliente.html'),
    path('altaCliente/', views.altaCliente, name='altaCliente.html'),
    path('bajaCliente/', views.bajaCliente, name='bajaCliente.html'),
    path('cambioCliente/', views.cambioCliente, name='cambioCliente.html'),
    path('listaCliente/', views.listaCliente, name='listaCliente.html'),

    path('proveedor/', views.proveedor, name='proveedor.html'),
    path('altaProveedor/', views.altaProveedor, name='altaProveedor.html'),
    path('bajaProveedor/', views.bajaProveedor, name='bajaProveedor.html'),
    path('cambioProveedor/', views.cambioProveedor, name='cambioProveedor.html'),
    path('listaProveedor/', views.listaProveedor, name='listaProveedor.html'),

    path('usuario/', views.usuario, name='usuario.html'),
    path('altaUsuario/', views.altaUsuario, name='altaUsuario.html'),
    path('bajaUsuario/', views.bajaUsuario, name='bajaUsuario.html'),
    path('cambioUsuario/', views.cambioUsuario, name='cambioUsuario.html'),
    path('listaUsuario/', views.listaUsuario, name='listaUsuario.html'),

    
]
