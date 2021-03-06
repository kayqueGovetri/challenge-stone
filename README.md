Stone Tech Challenge
===========================================

## Introdução
Aqui está o desenvolvimento requerido no desafio tech pela Stone, se baseia numa lista de compras
e uma lista de emails, possuindo os seguintes requisitos:

- Validar que não exista algum e-mail duplicado.
- Validar que nenhuma das listas esteja vazia.
- Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por sua quantidade
e somar todos os itens.
- Validar que a quantidade e valor de um item não sejam negativos.
- Dividir o valor de forma igual entre a quantidade de e-mails. 
- Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve
pagar nessa conta.
- Ter testes unitários.

## Setup

É necessário instalar previamente:

- [**Python 3.8.10**](https://www.python.org/downloads/release/python-3810/)
- [**Pip 22.1.12**](https://packaging.python.org/en/latest/tutorials/installing-packages/)

## Setup
Na raiz do projeto:

- Crie o virtualenv da aplicação:
  - ```python3 -m venv venv```
- Utilize o comando para ativar o virtualenv:
  - ```source venv/bin/activate```
  - Alerta: Caso você não utilize linux, siga o [guia](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/)
- Ainda na raiz do projeto, utilize o comando ```make install``` para instalar as dependências.

## Execução


Após a instalação, executar o arquivo **main.py** que está na raiz com o Python3.

É possível alterar as listas do mesmo arquivo (lista de itens e lista de emails).

```commandline
make run
```

## Testes
A aplicação utiliza o Pytest (que já está sendo instalado no requirements txt), será possível executar os testes a partir
do seguinte comando:
```commandline
make test
```
