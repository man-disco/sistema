from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from cadastros.models import Cadastro
from .models import Venda


# Create your views here.
@login_required(login_url='login')
@permission_required('vendas.view_venda', raise_exception=True)
def index(request):
    """"""
    return render(request, 'index.html')


@login_required(login_url='login')
@permission_required('vendas.view_venda', raise_exception=True)
def visualizar_vendas_cliente(request, cadastro_id):
    """"""
    try:
        cliente = Cadastro.objects.get(id=cadastro_id)
    except Cadastro.DoesNotExist:
        raise Http404("Cadastro não existe...")
    vendas = Venda.objects.filter(cliente=cliente).order_by('data_da_venda')
    context = {'cliente': cliente, 'vendas': vendas}
    return render(request, 'vendas_cliente.html', context)
