from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from cars.models import Marca, Carro


class TemplateHome(TemplateView):
    template_name = "index.html"


# Marca
class ListMarca(ListView):
    model = Marca


class CreateMarca(CreateView):
    model = Marca
    fields = ('nome',)
    success_url = reverse_lazy('list-marca')


class UpdateMarca(UpdateView):
    model = Marca
    fields = ('nome',)
    success_url = reverse_lazy('list-marca')


class DeleteMarca(DeleteView):
    model = Marca
    success_url = reverse_lazy('list-marca')


# Carro
class CreateCarro(CreateView):
    model = Carro
    fields = ('nome', 'modelo', 'marca', 'dono',)
    success_url = reverse_lazy('list-carro')

class ListCarro(ListView):
    model = Carro


class UpdateCarro(UpdateView):
    model = Carro
    fields = ('nome', 'modelo', 'marca', 'dono',)
    success_url = reverse_lazy('list-carro')


class DeleteCarro(DeleteView):
    model = Carro
    success_url = reverse_lazy('list-carro')