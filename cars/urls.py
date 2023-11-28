from django.urls import path

from cars.views import ListMarca, TemplateHome, CreateMarca, UpdateMarca, DeleteMarca

urlpatterns = [
    path('', TemplateHome.as_view() , name='home'),
    path('marca/', ListMarca.as_view(), name='list-marca'),
    path('marca/new/', CreateMarca.as_view(), name='create-marca'),
    path('marca/edit/<int:pk>', UpdateMarca.as_view(), name='update-marca'),
    path('marca/delete/<int:pk>', DeleteMarca.as_view(), name='delete-marca'),
]