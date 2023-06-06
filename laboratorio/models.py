# Version: 1.0
from django.db import models
# Create your models here.
class producto(models.Model):
    id              = models.AutoField(primary_key=True)
    fecha           = models.DateField(null=True, blank=True, verbose_name="Fecha de entrada")
    ref_fabricante  = models.CharField(max_length=30, null=True, blank=True, verbose_name="Referencia fabricante")
    nombre          = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nombre")
    caracteristica1 = models.CharField(max_length=30, null=True, blank=True, verbose_name="Caracteristica 1")
    caracteristica2 = models.CharField(max_length=30, null=True, blank=True, verbose_name="Caracteristica 2")
    familia         = models.CharField(max_length=30, null=True, blank=True, verbose_name="Familia")
    tipo            = models.CharField(max_length=30, null=True, blank=True, verbose_name="Tipo")
    marca           = models.CharField(max_length=30, null=True, blank=True, verbose_name="Marca")
    u_entrega       = models.CharField(max_length=30, null=True, blank=True, verbose_name="Unidad de entrega")
    stock_min       = models.IntegerField(null=True, blank=True, verbose_name="Stock minimo")
    stock_actual    = models.IntegerField( null=True, blank=True, verbose_name="Stock actual")
    precio          = models.IntegerField(null=True, blank=True,verbose_name="Precio")
    cantidad        = models.IntegerField(null=True, blank=True,verbose_name="Cantidad")
    albaran         = models.CharField(max_length=30, null=True, blank=True,verbose_name="Albaran")
    factura         = models.CharField(max_length=30, null=True, blank=True,verbose_name="Factura")
    proveedor       = models.CharField(max_length=30, null=True, blank=True,verbose_name="Proveedor")
    quien_entrega   = models.CharField(max_length=30, null=True, blank=True,verbose_name="Quien entrega")
    quien_recibe    = models.CharField(max_length=30, null=True, blank=True,verbose_name="Quien recibe")
    
    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    id           = models.AutoField(primary_key=True)
    nombre       = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nombre")
    apellido     = models.CharField(max_length=30, null=True, blank=True, verbose_name="Apellido")
    email        = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Email")
    password     = models.CharField(max_length=30, null=True, blank=True, verbose_name="Password")
    fecha_alta   = models.DateField(null=True, blank=True, verbose_name="Fecha de alta AAAA-MM-DD")
    fecha_baja   = models.DateField(null=True, blank=True, verbose_name="Fecha de baja AAAA-MM-DD")
    tipo_usuario = models.CharField(max_length=30, null=True, blank=True, verbose_name="Tipo de usuario")
    estado       = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.nombre

class cliente(models.Model):
    id         = models.AutoField(primary_key=True)
    nombre     = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nombre")
    email      = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Email")
    password   = models.CharField(max_length=30, null=True, blank=True, verbose_name="Password")
    fecha_alta = models.DateField(null=True, blank=True, verbose_name="Fecha de alta AAAA-MM-DD")
    fecha_baja = models.DateField(null=True, blank=True, verbose_name="Fecha de baja AAAA-MM-DD")
    def __str__(self):
        return self.nombre
    
class proveedor(models.Model):
    id         = models.AutoField(primary_key=True)
    nombre     = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nombre")
    email      = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Email")
    fecha_alta = models.DateField(null=True, blank=True, verbose_name="Fecha de alta AAAA-MM-DD")
    fecha_baja = models.DateField(null=True, blank=True, verbose_name="Fecha de baja AAAA-MM-DD")
    def __str__(self):
        fila = "Nombre: " + self.nombre + " Email: " + self.email
        return fila
    
# Borrado de imagenes
# def delete(self, using=None, keep_parents=False):
#     self.imagen.storage.delete(self.imagen.name)
#     super().delete( )