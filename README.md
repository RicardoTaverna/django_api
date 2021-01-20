# Projeto Django-API
Criado um serviço que recebe dados através de um endpoint, e de acordo com o cliente salva os dados em seus respectivos bancos de dados.

## Executar o projeto localmente

### Start dos bancos de dados
Você pode rodar qualquer um dos comandos abaixo para criar os bancos de dados localmente, entre na pasta scr em seguida:
- docker-compose up
- make run

---
### Configurações do python
Criar um ambiente virtual para instalar os requisitos.
<br />
**_Observações_** : O arquivo de requirements foi criado utilizando python 3.9, versões anteriores do python podem ter incompatibilidade

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

>**importante**
- acessar com o super usuário localhost:8000/admin
- criar dois novos usuários
    - _username_: varejao
    - _username_: macapa
---
### Fluxo para enviar dados
Com os dois usuários criados e suas respectivas senhas em mão seguir os seguintes passos:
- Gerar token de autenticação para o usuário pelo endpoint _localhost:8000/api/token/_ utilizando o username e senha
- Adicionar o token ao Bearer de autenticação do endpoint _localhost:8000/api/contacts/_
- Enviar o payload referente ao usuário (usuário varejao: payload contacts-varejao, usuário macapa: payload contacts-macapa) pelo endpoint _localhost:8000/api/contacts/_
>**importante:** gerar o token para um usuario e em seguida efetuar o disparo do seu payload, pois o token expira a cada 60 segundos.


---
## Endpoints

#### Acesso ao painel administrador
> localhost:8000/admin/

---
#### Endpoint para adicionar contados
> localhost:8000/api/contacts/

#### **_payload_:**
```json
{
    "contacts" : [
        {
            "name": "string",
            "cellphone": "string"
        }
    ]
}
```
#### _necessita token de autenticação Bearer_
---
#### Endpoint para gerar token de autenticação
>localhost:8000/api/token/
#### **_payload_:**
```json
{
  "username": [
    "This field is required."
  ],
  "password": [
    "This field is required."
  ]
}
```
---
#### Endpoint para refresh do token de autenticação
>api/token/refresh/
#### **_payload_:**
```json
{
  "refresh": [
    "This field is required."
  ]
}
```
---
#### Endpoint para verificar token de autenticação
>api/token/verify/
#### **_payload_:**
```json
{
  "token": [
    "This field is required."
  ]
}
```
<br />

> **Muito Importante**:
> Caso rode esse projeto no Windows, é necessário entrar na arquivo _src/api/settings.py_ e trocar o host do banco de dados default _(linha 85)_ de '0.0.0.0' para 'localhost'
