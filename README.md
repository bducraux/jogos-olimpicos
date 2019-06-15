# Jogos Olímpicos - API

API simples para cadastro de competiçoes, atletas e resultados dos atletas, podendo acessar o resultado da competiçao a qualquer momento.

Por ser uma API simples, resolvi manter o código o mais simples possível, aproveitando ao máxio o pode do Django e do Django-Rest-Framework, mantendo a estrutura original do Django para os Models e Views.

# Instalação e Configuração

Após clonar ou fazer o download do projeto, dentro do diretório do projeto rode o comando:

`pip install -r requirements.txt`

depois execute:

`python manage.py migrate`

Crie um super usuário:

`python manage.py createsuperuser`

# Rodando e acessando a aplicação
`python manage.py runserver`

A aplicação poderá ser acessada no endereço: http://127.0.0.1:8000/

### Página do Admin
http://127.0.0.1:8000/admin/

# Rodando testes
`python manage.py test`

# Documentação da API
`http://127.0.0.1:8000/docs/`