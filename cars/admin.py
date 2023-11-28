from django.contrib import admin

from cars.models import Marca, Carro, Loja, ServicoPrestado

admin.site.register(Marca)
admin.site.register(Carro)
admin.site.register(Loja)
admin.site.register(ServicoPrestado)