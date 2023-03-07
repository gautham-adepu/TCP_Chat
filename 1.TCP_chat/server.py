import socket
import threading

host = "127.0.0.1"
port = 54321

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []
userNames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            userName = userNames[index]
            userNames.remove(userName)
            broadcast(f'{userNames} Left the chat'.encode('ascii'))
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        client.send('name'.encode('ascii'))
        userName = client.recv(1024).decode('ascii')
        userNames.append(userName)
        clients.append(client)
        print(f'Username of the client is {userName}')
        broadcast(f'{userName} Joined the chat'.encode('ascii'))
        client.send("connected to the server!".encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
