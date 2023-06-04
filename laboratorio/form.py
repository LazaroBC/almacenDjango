from django import forms
from .models import producto, cliente, proveedor, usuario


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = '__all__'

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'