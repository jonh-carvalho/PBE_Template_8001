# models.py

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    departamentos = models.ManyToManyField('Departamento')
    marcas = models.ManyToManyField('Marca')
    faixas_etarias = models.ManyToManyField('FaixaEtaria')
    sexos = models.ManyToManyField('Sexo')

    def __str__(self):
        return self.nome
    
class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class FaixaEtaria(models.Model):
    faixa = models.CharField(max_length=20)

    def __str__(self):
        return self.faixa

class Sexo(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
