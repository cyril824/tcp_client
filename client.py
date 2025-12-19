# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", 4242))

# data = client.recv(1024)
# print("Serveur :", data.decode())
# client.send(b"Hello !")

import socket

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 4242))

    data = client.recv(1024)
    print("Serveur :", data.decode())
    message = input("Ton message (ou tape 'exit' pour fermer) : ")
    
    if message.lower() == 'exit':
        client.send(b"Deconnexion")
        client.close()
        break

    client.send(message.encode())

    client.close()