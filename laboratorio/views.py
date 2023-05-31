from django.shortcuts import render
from django.http import HttpResponse
from .models import producto, cliente, proveedor, usuario
# Create your views here.

# def inicio(request):
#     return render(request, 'html/inicio.html')

# Vistas de producto
# def producto(request):
#     return render(request, 'html/producto.html')

# def altaProducto(request):
#     return render(request, 'html/altaProducto.html')

# def bajaProducto(request):
#     return render(request, 'html/bajaProducto.html')

# def cambioProducto(request):
#     return render(request, 'html/cambioProducto.html')

# def listaProducto(request):
#     return render(request, 'html/listaProducto.html')

# Vistas de cliente
# def cliente(request):
#     return render(request, 'html/cliente.html')

# def altaCliente(request):
#     return render(request, 'html/altaCliente.html')

# def bajaCliente(request):
#     return render(request, 'html/bajaCliente.html')

# def cambioCliente(request):
#     return render(request, 'html/cambioCliente.html')

# def listaCliente(request):
#     return render(request, 'html/listaCliente.html')

# # Vistas de proveedor
# def proveedor(request):
#     return render(request, 'html/proveedor.html')

# def altaProveedor(request):
#     return render(request, 'html/altaProveedor.html')

# def bajaProveedor(request):
#     return render(request, 'html/bajaProveedor.html')

# def cambioProveedor(request):
#     return render(request, 'html/cambioProveedor.html')

# def listaProveedor(request):
#     return render(request, 'html/listaProveedor.html')

# # Vistas de usuario
# def usuario(request):
#     return render(request, 'html/usuario.html')

# def altaUsuario(request):
#     return render(request, 'html/altaUsuario.html')

# def bajaUsuario(request):
#     return render(request, 'html/bajaUsuario.html')

# def cambioUsuario(request):
#     return render(request, 'html/cambioUsuario.html')

# def listaUsuario(request):
#     return render(request, 'html/listaUsuario.html')

def login(request):
    return render(request, 'html/login.html')

# Plantillas base y pruebas 
def inicio(request):
    return render(request, 'inicio.html')

# Productos
def listaProducto(request):
    productos = producto.objects.all()
    return render(request, 'html/producto/listaProducto.html',{'productos':productos})

def crearProducto(request):
    return render(request, 'html/producto/crearProducto.html')

def editarProducto(request):
    return render(request, 'html/producto/editarProducto.html')

# Clientes

def listaCliente(request):
    clientes = cliente.objects.all()
    return render(request, 'html/cliente/listaCliente.html',{'clientes':clientes})

def crearCliente(request):
    return render(request, 'html/cliente/crearCliente.html')

def editarCliente(request):
    return render(request, 'html/cliente/editarCliente.html')

# Proveedores

def listaProveedor(request):
    proveedores = proveedor.objects.all()
    print(proveedores)
    return render(request, 'html/proveedor/listaProveedor.html',{'proveedores':proveedores})

def crearProveedor(request):
    return render(request, 'html/proveedor/crearProveedor.html')

def editarProveedor(request):
    return render(request, 'html/proveedor/editarProveedor.html')

# Usuarios

def listaUsuario(request):
    usuarios = usuario.objects.all()
    return render(request, 'html/usuario/listaUsuario.html',{'usuarios':usuarios})

def crearUsuario(request):
    return render(request, 'html/usuario/crearUsuario.html')

def editarUsuario(request):
    return render(request, 'html/usuario/editarUsuario.html')
