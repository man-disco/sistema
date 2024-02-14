from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from cadastros.models import Cadastro

# Create your views here.


def deslogar(request):
    """Desloga um usuário do sistema."""
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('login'))

@login_required(login_url='login')
def perfil(request):
    """Retorna uma página que mostra informações e permissões de um usuário."""
    return render(request, 'usuarios/perfil.html')
