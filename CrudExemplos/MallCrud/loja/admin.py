from django.contrib import admin
from loja.models import Cliente, Departamento, FaixaEtaria, Marca, Sexo, Produto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(FaixaEtaria)
admin.site.register(Marca)
admin.site.register(Sexo)
admin.site.register(Produto)