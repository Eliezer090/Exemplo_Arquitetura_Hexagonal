# Exemplo de Arquitetura Hexagonal com Python e Flask

## Objetivo do projeto
- Como principal objetivo foi aprender como funciona a arquitetura hexagonal e como ela pode ser aplicada com Python e Flask.
- Segundo ponto foi a inexistência de exemplos de arquitetura hexagonal aplicada com Python.
- Por final é demonstrar como esta arquitetura pode ser aplicada com Python em uma simples API de pedido, e como podemos desacoplar todas as partes de um projeto facilmente.

## Principais tecnologias e bibliotecas utilizadas
- Foi utilizado a linguagem [python](https://www.python.org/) para desenvolver o projeto.
- Foi consutruido utilizando o [poetry](https://poetry.eustace.io/) para gerenciar as dependências.
- Foi utilizado o [Flask](https://flask.palletsprojects.com/) para servir a API.
- Foi utilizado o [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/) para separar as rotas da API.
- Foi utilizado o [Pytest](https://pytest.org/) para gerenciar os testes.


## Explicação da arquitetura hexagonal
- Foi utilizado a arquitetura hexagonal para desenvolver o projeto, como estudo foi utilizado este [post](https://herbertograca.com/2017/09/14/ports-adapters-architecture/) para entendimento da arquitetura.
- No print abaixo tem uma exemplicação de como seria a Arquitetura Hexagonal:<br>
![Hexagonal Architecture](https://user-images.githubusercontent.com/36082343/173716095-28cfabae-02aa-4272-ad8f-13ab729c3dbe.png)
- Toda a aplicação pode ser separada em 3 niveis:
    - Web(Lado esquerdo do print acima)
        - Este ponto seria a entrada seria o que o cliente iria chamar para comunicar com a api, esta parte além de receber a requisição por diferentes entradas que podemos ter faria também o pré-processamento, em resumo recebe e entende o que o cliente enviou, para assim montar a comunicação com o "back-end(Domain)" para processar.

    - Domain(Parte do meio do print acima)
        - Este ponto seria o processamento da requisição, esta parte recebe o que o lado esquerdo recebeu do cliente e processa de fato, comunicando com os meios externos(Banco de dados, serviços de email, etc.)

    - Adapters(Parte da direita do print acima)
        - Aqui seria feito a comunicação com aplicações externas do nosso código, ou seja, tudo o que precisa ser solicitado/enviado exterdo da API será responsabilidade desta parte realizar a implementação.
- Com estas separações descritas acima podemos ter uma aplicação muito mais flexivel e aberta para modificações e inclusões.

## Como executar o projeto
- Para poder iniciar é preciso ter instalado as dependências abaixo:
    - [Python](https://www.python.org/)
    - [Pip](https://pip.pypa.io/)
    - [Poetry](https://poetry.eustace.io/)
    - [Git](https://git-scm.com/)
- Após ter instalado as dependências pode ser clonado o repositório do projeto:
######
    git clone https://github.com/Eliezer090/Exemplo_Arquitetura_Hexagonal.git
- Para executar o projeto é preciso estar dentro da pasta do projeto e rodar o comando abaixo para definir que queremos criar o ambiente virtual dentro da pasta do projeto:
######
    poetry config virtualenvs.in-project true
- Após isso pode ser executado a criação e ativação do ambiente virtual:
######
    poetry shell
- Após pode ser executado o comando abaixo para instalar as dependências do projeto(O poetry fará todo o trabalho para nós):
######
    poetry install
- Precisa ser definido também uma variavel global para que o Flask consiga encontrar quem inicia o projeto:
######
    export FLASK_APP=src/main.py
- Após isso pode ser executado o comando abaixo para executar o projeto:
######
    poe start
#####
- Após isso se tudo deu certo, deve estar executando o projeto no endereço http://127.0.0.1:5000
    - Rotas do projeto:
        - A rota abaixo retorna um json com todos os pedidos cadastrados:
            - http://127.0.0.1:5000/api/get_pedidos
        - Para a rota abaixo é preciso enviar um json no body da requisição, com o pedido que deseja ser cadastrado:
            - Content-Type: application/json
            - Conteudo:
                - {"id": 0, "title": "Computador"}
            - http://127.0.0.1:5000/api/post_pedido

            
