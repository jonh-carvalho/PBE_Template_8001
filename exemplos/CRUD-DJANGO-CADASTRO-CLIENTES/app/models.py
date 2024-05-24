from django.db import models

# Create your models here.
class Pessoa(models.Model):
    avatar = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, blank=False)
    descricao = models.TextField()
    whatsapp = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome