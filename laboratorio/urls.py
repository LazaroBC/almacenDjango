from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('inicio/', views.inicio, name='inicio'),

    # path('producto/', views.producto, name='producto'),
    # path('altaProducto/', views.altaProducto, name='altaProducto'),
    # path('bajaProducto/', views.bajaProducto, name='bajaProducto'),
    # path('cambioProducto/', views.cambioProducto, name='cambioProducto'),
    # path('listaProducto/', views.listaProducto, name='listaProducto'),

    # path('cliente/', views.cliente, name='cliente'),
    # path('altaCliente/', views.altaCliente, name='altaCliente'),
    # path('bajaCliente/', views.bajaCliente, name='bajaCliente'),
    # path('cambioCliente/', views.cambioCliente, name='cambioCliente'),
    # path('listaCliente/', views.listaCliente, name='listaCliente'),

    # path('proveedor/', views.proveedor, name='proveedor'),
    # path('altaProveedor/', views.altaProveedor, name='altaProveedor'),
    # path('bajaProveedor/', views.bajaProveedor, name='bajaProveedor'),
    # path('cambioProveedor/', views.cambioProveedor, name='cambioProveedor'),
    # path('listaProveedor/', views.listaProveedor, name='listaProveedor'),

    # path('usuario/', views.usuario, name='usuario'),
    # path('altaUsuario/', views.altaUsuario, name='altaUsuario'),
    # path('bajaUsuario/', views.bajaUsuario, name='bajaUsuario'),
    # path('cambioUsuario/', views.cambioUsuario, name='cambioUsuario'),
    # path('listaUsuario/', views.listaUsuario, name='listaUsuario'),

    path('login/', views.login, name='login'),

    # Plantillas base y pruebas
    path('inicio/', views.inicio, name='inicio'),
    path('listaProducto/', views.listaProducto, name='listaProducto'),
    path('crearProducto/', views.crearProducto, name='crearProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),

    path('listaCliente/', views.listaCliente, name='listaCliente'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('editarCliente/', views.editarCliente, name='editarCliente'),

    path('listaProveedor/', views.listaProveedor, name='listaProveedor'),
    path('crearProveedor/', views.crearProveedor, name='crearProveedor'),
    path('editarProveedor/', views.editarProveedor, name='editarProveedor'),

    path('listaUsuario/', views.listaUsuario, name='listaUsuario'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    path('editarUsuario/', views.editarUsuario, name='editarUsuario'),

]
