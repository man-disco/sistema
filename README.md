# Como Instalar e Executar o Projeto
## Clonar o Repositório:
Rode o comando: `git clone https://github.com/seu-usuario/seu-projeto.git`

Depois: `cd seu-projeto`

## Criar e Ativar um Ambiente Virtual:
Rode o comando: `python -m venv venv`

Rode o comando: `source venv/bin/activate  # No Windows: venv\Scripts\activate`

## Instalar Dependências:
Rode o comando: `pip install -r requirements.txt`

## Realizar as Migrações do Banco de Dados:
Rode o comando: `python manage.py migrate`

## Criar um Superusuário:
Rode o comando: `python manage.py createsuperuser`

## Executar o Servidor Localmente:
Rode o comando: `python manage.py runserver`

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
