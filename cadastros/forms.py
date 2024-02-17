from django import forms
from .models import Cadastro
from phonenumber_field.modelfields import PhoneNumberField


class NovoCadastro(forms.ModelForm):
    """Cria um novo cadastro."""

    class Meta:
        model = Cadastro
        exclude = ['criado_por', 'alterado_por']
        
        widgets = {
            'nome': forms.Textarea(attrs={'rows': 1, 'placeholder': 'Seu nome'}),
            'endereço': forms.Textarea(attrs={'cols': 40, 'placeholder': 'Ex: Avenida da rosa, Nº 33'}),
            'data_nascimento': forms.DateInput(attrs={'placeholder': 'Ex: 99/99/9999'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Ex: (99) 99999-9999'}),
        }
        input_formats = {
            'data_nascimento': ['%m/%d/%Y'],
        }

class DeletarCadastro(forms.Form):
    """Deleta um cadastro."""
    
    deletar = forms.DurationField()
