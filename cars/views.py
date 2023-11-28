from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from cars.models import Marca


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