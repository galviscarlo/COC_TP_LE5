from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'web/index.html', context={})

def recetas(request):
    return HttpResponse("Hola")

def nosotros(request):
    return HttpResponse("Hola")

def contacto(request):
    return HttpResponse("Hola")