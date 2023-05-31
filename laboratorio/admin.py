from django.contrib import admin
from laboratorio.models import producto, usuario, cliente, proveedor
# Register your models here.
admin.site.register(producto)
admin.site.register(usuario)
admin.site.register(cliente)
admin.site.register(proveedor)

# Superuser: admin
# Email: admin@admin.com
# Password: admin


