from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subir/', views.subir, name="subir"),
    path('editar/', views.editar, name="editar"),
    path('recetas/', views.recetas, name="recetas"),

]