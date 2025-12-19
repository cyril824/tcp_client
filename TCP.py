import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4242))
server.listen(5)

print("Serveur TCP en écoute sur le port 4242...")

while True:
    client, addr = server.accept()
    print(f"Nouvelle connexion de {addr}")

    client.send(b"Bienvenue sur le serveur TCP! (Session ouverte)\n")

    while True:
        data = client.recv(1024)

        if not data:
            break
            
        print("Reçu:", data.decode('utf-8'))

    print(f"Déconnexion de {addr}")
    client.close()