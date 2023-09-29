import socket
import threading

def handle_client(client_socket, clients):
    while True:
        try:
            data = client_socket.recv(10240)
            message = data.decode('utf-8')
            print('mensagem recebida:', message)

            if message[:4] == 'EXIT':
                for client in clients:
                    client.send(message[5:].encode('utf-8'))

                clients.remove(client_socket)
                client_socket.close()
            elif message[:5] == 'ENTER':
                for client in clients:
                    client.send(message[6:].encode('utf-8'))
            else:
                nickname_space_index = message.find(' ')
                nickname = message[:nickname_space_index]
                resp = nickname + ': ' + message[nickname_space_index + 1:]

                for client in clients:
                    client.send(resp.encode('utf-8'))
        except Exception as e:
            print('matando thread e fechando socket')
            try:
                clients.remove(client_socket)
                client_socket.close()
            except Exception as e:
                pass
            break

HOST = '127.0.0.1'
PORT = 65432
MAX_CLIENTS = 4

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen(MAX_CLIENTS)
    print(f"Server escutando {HOST}:{PORT}")

    clients = []
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Conexão de {client_address} aceita")
            
            clients.append(client_socket)
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket,clients))
            client_thread.start()
        except Exception as e:
            print(f"Exceção: {e}\nDesligando server")
            break

    for client in clients:
        client.close()
    server_socket.close()