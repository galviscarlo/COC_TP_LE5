from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subir/', views.RecetaCreateView.as_view(), name="subir"),
    path('recetas/', views.RecetaListView.as_view(), name="recetas"),
    path('detalle/<pk>', views.RecetaDetailView.as_view(), name="receta_detalle"),
    path('editar/<pk>', views.RecetaUpdateView.as_view(), name="editar"),
    path('eliminar/<pk>', views.RecetaDeleteView.as_view(), name="eliminar"),
]