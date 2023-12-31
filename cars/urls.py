from django.urls import path

from cars.views import ListMarca, TemplateHome, CreateMarca, UpdateMarca, DeleteMarca, ListCarro, CreateCarro, \
    UpdateCarro, DeleteCarro

urlpatterns = [
    path('', TemplateHome.as_view(), name='home'),
    path('marca/', ListMarca.as_view(), name='list-marca'),
    path('marca/new/', CreateMarca.as_view(), name='create-marca'),
    path('marca/edit/<int:pk>', UpdateMarca.as_view(), name='update-marca'),
    path('marca/delete/<int:pk>', DeleteMarca.as_view(), name='delete-marca'),
    path('carro/', ListCarro.as_view(), name='list-carro'),
    path('carro/new/', CreateCarro.as_view(), name='create-carro'),
    path('carro/edit/<int:pk>', UpdateCarro.as_view(), name='update-carro'),
    path('carro/delete/<int:pk>', DeleteCarro.as_view(), name='delete-carro'),
]