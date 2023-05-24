from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio2/', views.inicio2, name='inicio2.html'),
]