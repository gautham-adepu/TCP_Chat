import socket
import threading

userName = input('Enter your name:')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 54321))

def receive():

    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'name':
                client.send(userName.encode('ascii'))
            else:
                print(message)
        except:
            print('An error has Occured!')
            client.close()
            break

def write():
    while True:
        message = f'{userName}:{input ("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()






