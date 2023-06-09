"""
URL configuration for almacen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('laboratorio.urls')),
    # path('inicio/', include('laboratorio.urls')),
    # path('producto/', include('laboratorio.urls')),
    # path('altaProducto/', include('laboratorio.urls')),
    # path('bajaProducto/', include('laboratorio.urls')),
    # path('cambioProducto/', include('laboratorio.urls')),
    # path('listaProducto/', include('laboratorio.urls')),
    # path('login/', include('laboratorio.urls')),
]
