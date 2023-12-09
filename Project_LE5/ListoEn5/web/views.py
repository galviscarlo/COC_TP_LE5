from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'web/index.html', context={})

def subir(request):
    return HttpResponse("Hola")

def editar(request):
    return HttpResponse("Hola")

def recetas(request):
    return HttpResponse("Hola")