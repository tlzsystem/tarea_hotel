from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Minuta

class MinutaDetail(DetailView):
    model = Minuta

class MinutaList(ListView):
    model = Minuta

class MinutaCreate(CreateView):
    model = Minuta
    fields = '__all__'
    success_url = '/minutas/'

class MinutaDelete(DeleteView):
    model = Minuta
    success_url = reverse_lazy('minuta-list')

class MinutaUpdate(UpdateView):
    model = Minuta
    success_url = reverse_lazy('minuta-list')
    fields = '__all__'



