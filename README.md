# Como Instalar e Executar o Projeto
## Clonar o Repositório:
Rode o comando: `git clone https://github.com/seu-usuario/seu-projeto.git`

Depois entre na pasta do projeto: `cd seu-projeto`

## Crie e Ative um Ambiente Virtual:
Rode o comando: `python -m venv venv`

Depois: `source venv/bin/activate`

No Windows: `venv\Scripts\activate`

## Instale as Dependências:
Rode o comando: `pip install -r requirements.txt`

## Realize as Migrações do Banco de Dados:
Rode o comando: `python manage.py migrate`

## Crie um Superusuário:
Rode o comando: `python manage.py createsuperuser`

## Execute o Servidor Localmente:
Rode o comando: `python manage.py runserver`

## Crie Dados Falsos Para Teste:
Rode o comando: `python manage.py shell < cria_cadastros.py`

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
