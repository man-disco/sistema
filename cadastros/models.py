from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Telefone(models.Model):
    """Modelo que valida um número de contato válido."""
    phone_regex = RegexValidator(
        regex=r'^\(\d{2}\) \d{5}-\d{4}$',
        message="Por favor, insira um número válido no formato especificado: (99) 99999-9999."
    )


class Cadastro(models.Model):
    """Modelo que armazena todas as informações de um cadastro."""

    OPC_SEXO = [
        ('M','Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhuma das opções')
    ]
    nome = models.CharField(max_length=80, blank=False, null=False)
    endereço = models.CharField(max_length=200, unique=True)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=OPC_SEXO, blank=False, null=False)
    telefone = models.CharField(validators=[Telefone.phone_regex], max_length=15, blank=True, null=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em= models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name='created_instances')
    alterado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_instances')

    class Meta:
        verbose_name_plural = 'cadastros'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'