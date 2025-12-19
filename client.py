import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 4242))

    data = client.recv(1024)
    if data:
        print("Serveur :", data.decode())

    while True:
        message = input("Ton message (ou tape 'exit' pour fermer) : ")
        
        if message.lower() == 'exit':
            break

        client.send(message.encode())

except ConnectionRefusedError:
    print("Erreur : Impossible de se connecter. Le serveur est-il bien lancé ?")
except ConnectionResetError:
    print("Erreur : La connexion a été coupée par le serveur.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")

finally:
    client.close()
    print("Connexion fermée.")