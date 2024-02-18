from faker import Faker
from random import choice, randint
from cadastros.models import Cadastro


OPC_SEXO = ['M', 'F', 'N']
fake = Faker('pt_BR')


def gera_numero_telefone():
    """"""
    códigos = [21, 34, 22, 19, 11, 67]
    código_sel = choice(códigos)
    primeira_parte = randint(90000, 98000)
    segunda_parte = randint(2000, 6000)
    número_formatado = f"({código_sel}) {primeira_parte}-{segunda_parte}"
    return número_formatado


def gera_cadastros(quantidade=20):
    """Gera uma quantia de cadastros falsos para popular o banco de dados."""
    for _ in range(quantidade):
        nome = fake.name()
        endereço = fake.address()
        sexo = choice(OPC_SEXO)
        data_nascimento = fake.date_of_birth()
        telefone = gera_numero_telefone()
        alterado_por = 'UsuárioTeste'
        criado_por = 'UsuárioTeste'
        cadastro = Cadastro.objects.create(nome=nome, endereço=endereço, sexo=sexo, telefone=telefone, data_nascimento=data_nascimento)


gera_cadastros()
        
     

