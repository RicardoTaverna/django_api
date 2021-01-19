# Projeto Django-API
[![Project Version][version-image]][version-url]
[![Python][Backend-image]][Backend-url]

## Executar o projeto localmente

### Start do bancos de dados
Você pode rodar qualquer um dos comandos abaixo para criar os bancos de dados localmente:
- docker-compose up
- make run

---
### Configurações do python
Criar um ambiente virtual para instalar os requisitos
__Observações__: O arquivo de requirements foi criado utilizando python 3.9, versões anteriores do python podem ter incompatibilidade

- pip install -r requirements

---
### Start do projeto
Para o correto funcionamento da API é necessário seguir os passos abaixo:

- entrar na pasta src
- executar as migrations da seguinte forma
    - python manage.py migrate
    - python manage.py migrate --database=postgres
    - python manage.py makemigrations
- criar um super usuário
    - python manage.py createsuperuser
    - escolher usuario e senha
- start do servidor localmente
    - python manage.py runserver

>*importante*
- acessar com o super usuário localhost:5000/admin
- criar dois novos usuários
    - _username_: varejao
    - _username_: macapa


---
## Endpoints