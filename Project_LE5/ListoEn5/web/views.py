from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Receta

# Vistas basadas en clase 

class RecetaListView(ListView):
    model = Receta
    context_object_name = 'listado_recetas'
    template_name = 'web/recetas.html'

class RecetaCreateView(CreateView):
    model = Receta
    template_name = 'web/subir.html'
    success_url = reverse_lazy('recetas')
    fields = '__all__' #['nombre', 'ingredientes']

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'web/receta_detalle.html'

class RecetaUpdateView(UpdateView):
    template_name= 'web/editar.html'
    model = Receta
    fields = '__all__'

    def get_success_url(self):
        return reverse('receta_detalle', kwargs={'pk': self.object.pk})
    
class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'web/eliminar.html'
    success_url = reverse_lazy('recetas')

   