import PySimpleGUI as sg
import socket
import threading
import time

def get_nickname():
    layout = [[sg.Text('Digite seu nome de usuário')],
            [sg.Input(key='-NICKNAME-')],
            [sg.Button('OK')]]

    window = sg.Window('Login', layout)

    nickname = ''
    while True:
        event, values = window.read()
        if event in (None, 'OK'):
            nickname = values['-NICKNAME-']
            break

    window.close()

    return nickname

def receive_message(client_socket, window, nickname):
    while True:
        try:
            data = client_socket.recv(10240)

            if not data:
                break

            msg = data.decode('utf-8')
            print('Mensagem recebida:', msg)

            if f'{nickname} saiu' in msg:
                client_socket.close()
                print('Fechando socket')
                break

            output = data.decode('utf-8') + '\n'
            window['-OUTPUT-'].update(output, append=True)
        except Exception as e:
            break

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

if __name__ == '__main__':
    nickname = get_nickname()

    layout = [[sg.Text('Usuário: ' + nickname)],
            [sg.Multiline(size=(50, 20), key='-OUTPUT-', disabled=True)],
            [sg.Input(size=(50, 1), key='-INPUT-')],
            [sg.Button('Enviar'), sg.Button('Sair')]]

    window = sg.Window('ChatRoom', layout)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    print(f"Conectado a {SERVER_HOST}:{SERVER_PORT}")

    enter_message = f'ENTER {nickname} entrou na sala!'
    client_socket.send(enter_message.encode('utf-8'))
    client_socket.recv(10240)

    send_thread = threading.Thread(target=receive_message, args=(client_socket, window, nickname))
    send_thread.start()

    while True:
        event, values = window.read()

        if event in (None, 'Sair'):
            exit_message = f'EXIT {nickname} saiu da sala!'
            client_socket.send(exit_message.encode('utf-8'))

            while send_thread.is_alive():
                pass

            break
        
        if event == 'Enviar':
            message = values['-INPUT-']
            window['-INPUT-'].update('')
            message = nickname + ' ' + message
            client_socket.send(message.encode('utf-8'))

    window.close()