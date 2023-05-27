from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

# Vistas de producto
def producto(request):
    return render(request, 'producto.html')

def altaProducto(request):
    return render(request, 'altaProducto.html')

def bajaProducto(request):
    return render(request, 'bajaProducto.html')

def cambioProducto(request):
    return render(request, 'cambioProducto.html')

def listaProducto(request):
    return render(request, 'listaProducto.html')

# Vistas de cliente
def cliente(request):
    return render(request, 'cliente.html')

def altaCliente(request):
    return render(request, 'altaCliente.html')

def bajaCliente(request):
    return render(request, 'bajaCliente.html')

def cambioCliente(request):
    return render(request, 'cambioCliente.html')

def listaCliente(request):
    return render(request, 'listaCliente.html')

# Vistas de proveedor
def proveedor(request):
    return render(request, 'proveedor.html')

def altaProveedor(request):
    return render(request, 'altaProveedor.html')

def bajaProveedor(request):
    return render(request, 'bajaProveedor.html')

def cambioProveedor(request):
    return render(request, 'cambioProveedor.html')

def listaProveedor(request):
    return render(request, 'listaProveedor.html')

# Vistas de usuario
def usuario(request):
    return render(request, 'usuario.html')

def altaUsuario(request):
    return render(request, 'altaUsuario.html')

def bajaUsuario(request):
    return render(request, 'bajaUsuario.html')

def cambioUsuario(request):
    return render(request, 'cambioUsuario.html')

def listaUsuario(request):
    return render(request, 'listaUsuario.html')