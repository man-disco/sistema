# Como Instalar e Executar o Projeto
## Clone o Repositório:
Rode o comando: 
`git clone https://github.com/man-disco/sistema-cad.git`

Depois entre na pasta do projeto: 
`cd sistema-cad/sistema`

## Crie e Ative um Ambiente Virtual:
Rode o comando: `python -m venv venv`

No Linux/Mac: `source venv/bin/activate`

No Windows: `venv\Scripts\activate.ps1`

## Instale as Dependências:
Rode o comando: 
`pip install -r requirements.txt`

## Realize as Migrações do Banco de Dados:
Rode o comando: `python manage.py migrate`

## Crie um Superusuário:
Rode o comando: `python manage.py createsuperuser`

## Execute o Servidor Localmente:
Rode o comando: `python manage.py runserver`

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
