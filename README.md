# REDES-ChatRoom
Projeto Python de chatroom utilizando sockets, threads e GUI com PySimpleGUI.

## Execução
Instruções de como utilizar a aplicação.

### Server
Inicialmente, é necessário executar o script do server. Para isso, o requisito é:
* Ter Python3 instalado.

Para executar o server, digite num terminal o comando:
* `python server.py`
  ou
* `python3 server.py`

Finalmente, o server estará executando e esperando por conexões de clientes.

**OBS**: Dentro do script, é especificado que o máximo de conexão de clientes no server é 4. Isso pode
ser alterado apenas mudando a constante `MAX_CLIENTS` no script `server.py`.

## Clients
Agora, para utilizar a sala de chat, é necessário executar o script do cliente. Para isso, os requisitos são:
* Ter Python3 instalado;
* Ter PySimpleGUI instalado.

Para instalar o PySimpleGUI, é necessário (em alguns SOs) estar em um ambiente virtual python. Então, para isso,
crie um ambiente virtual python e ative-o de acordo com as [instruções](https://docs.python.org/3/library/venv.html).

Então, com o ambiente python ativado, digite o comando:
* `pip intall pysimplegui` ou
* `pip3 install pysimplegui`

Finalmente, para executar o cliente, simplesmente execute o script:
* `python client.py` ou
* `python3 client.py`

Escolha um apelido para usar no chat (NÃO PODE TER ESPAÇO!) e pronto, você está conectado à sala de chat!
