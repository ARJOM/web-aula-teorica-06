from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    pass

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    nome = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=False)
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " - " + self.modelo

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


class Loja(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.TextField()
    servicos = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Loja"
        verbose_name_plural = "Lojas"

class ServicoPrestado(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    custo = models.FloatField()

    def __str__(self):
        return self.loja.nome + " - " + self.carro.nome

    class Meta:
        verbose_name = "Serviço Prestado"
        verbose_name_plural = "Seviços Prestados"
