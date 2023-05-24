from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<!DOCTYPE html><head><title>Document</title></head><body><h1>Almacen Laboratorio</h1></body></html>")
