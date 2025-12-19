# import socket


# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 4242))
# server.listen(5)


# print("Serveur TCP en écoute sur le port 4242...")


# client, addr = server.accept()
# print(f" Connexion de {addr}")
# client.send(b"Bievenue sur le serveur TCP!\n")

# data = client.recv(1024)
# print("Reçu:", data)

# client.close()



import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4242))
server.listen(5)

print("Serveur TCP en écoute sur le port 4242...")

while True:
    client, addr = server.accept()
    print(f"Connexion de {addr}")

    client.send(b"Bienvenue sur le serveur TCP!\n")
    data = client.recv(1024)

    print("Reçu:", data.decode('utf-8'))
    
    client.close()

