from django.db import models
from cadastros.models import Cadastro

# Create your models here.
class Venda(models.Model):
    """Representa uma produto comprado por um cliente cadastrado"""
    produto = models.CharField(max_length=100, null=False, blank=False)
    valor_produto = models.FloatField(null=False, blank=False)
    data_da_venda = models.DateField(null=False, blank=False)
    cliente = models.ForeignKey(Cadastro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto}"