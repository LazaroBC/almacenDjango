from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import producto, cliente, proveedor, usuario
from .form import FormularioProducto, FormularioCliente, FormularioProveedor, FormularioUsuario


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
    return render(request, 'html/producto/listaProducto.html', {'productos': productos})

def crearProducto(request):
    formulario = FormularioProducto(
        request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaProducto')
    return render(request, 'html/producto/crearProducto.html', {'formulario': formulario})

def editarProducto(request, id):
    editProducto = producto.objects.get(id=id)
    formulario = FormularioProducto(request.POST or None, instance=editProducto)
    if formulario.is_valid():
        formulario.save()  # Guardar los cambios en la base de datos
        return redirect('listaProducto')
    return render(request, 'html/producto/editarProducto.html', {'formulario': formulario})

def eliminarProducto(request, id):
    producto.objects.filter(id=id).delete()
    return redirect('listaProducto')


# Clientes

def listaCliente(request):
    clientes = cliente.objects.all()
    return render(request, 'html/cliente/listaCliente.html', {'clientes': clientes})

def crearCliente(request):
    formulario = FormularioCliente(
        request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaCliente')
    return render(request, 'html/cliente/crearCliente.html', {'formulario': formulario})

def editarCliente(request, id):
    editCliente = cliente.objects.get(id=id)
    formulario = FormularioCliente(request.POST or None, instance=editCliente)
    if formulario.is_valid():
        formulario.save()  # Guardar los cambios en la base de datos
        return redirect('listaCliente')
    return render(request, 'html/cliente/editarCliente.html', {'formulario': formulario})

def eliminarCliente(request, id):
    productoEliminado = cliente.objects.get(id=id)
    productoEliminado.delete()
    return redirect('listaCliente')


# Proveedores

def listaProveedor(request):
    proveedores = proveedor.objects.all()
    print(proveedores)
    return render(request, 'html/proveedor/listaProveedor.html', {'proveedores': proveedores})

def crearProveedor(request):
    formulario = FormularioProveedor(
        request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaProveedor')
    return render(request, 'html/proveedor/crearProveedor.html', {'formulario': formulario})

def editarProveedor(request):
    return render(request, 'html/proveedor/editarProveedor.html')

def editarProveedor(request, id):
    editProveedor = proveedor.objects.get(id=id)
    formulario = FormularioProveedor(request.POST or None, instance=editProveedor)
    if formulario.is_valid():
        formulario.save()  # Guardar los cambios en la base de datos
        return redirect('listaProveedor')
    return render(request, 'html/proveedor/editarProveedor.html', {'formulario': formulario})

def eliminarProveedor(request, id):
    proveedorEliminado = proveedor.objects.get(id=id)
    proveedorEliminado.delete()
    return redirect('listaProveedor')


# Usuarios

def listaUsuario(request):
    usuarios = usuario.objects.all()
    return render(request, 'html/usuario/listaUsuario.html', {'usuarios': usuarios})

def crearUsuario(request):
    formulario = FormularioUsuario(
        request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaUsuario')
    return render(request, 'html/usuario/crearUsuario.html', {'formulario': formulario})

def editarUsuario(request, id):
    editUsuario = usuario.objects.get(id=id)
    formulario = FormularioUsuario(request.POST or None, instance=editUsuario)
    if formulario.is_valid():
        formulario.save()  # Guardar los cambios en la base de datos
        return redirect('listaUsuario')
    return render(request, 'html/usuario/editarUsuario.html', {'formulario': formulario})

def eliminarUsuario(request, id):
    usuarioEliminado = usuario.objects.get(id=id)
    usuarioEliminado.delete()
    return redirect('listaUsuario')
