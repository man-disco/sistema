from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from cadastros.models import Cadastro
from .models import Venda


# Create your views here.
@login_required(login_url='login')
@permission_required('vendas.view_venda', raise_exception=True)
def index(request):
    """"""
    return HttpResponse("Vendas aqui :)")


@login_required(login_url='login')
@permission_required('vendas.view_venda', raise_exception=True)
def visualizar_vendas_cliente(request, cadastro_id):
    """"""
    try:
        cliente = get_object_or_404(Cadastro, pk=cadastro_id)
    except Exception as error:
        HttpResponse(f'Erro! {{error}}')
    vendas = Venda.objects.filter(cliente=cliente).order_by('data_da_venda')
    context = {'cliente': cliente, 'vendas': vendas}
    return render(request, 'vendas_cliente.html', context)
