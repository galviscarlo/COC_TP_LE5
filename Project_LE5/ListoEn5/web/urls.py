from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recetas/', views.recetas, name="recetas"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
]