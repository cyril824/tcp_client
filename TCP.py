import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("127.0.0.1", 4242))
    server.listen(5)
    print("Serveur TCP en écoute sur le port 4242...")
    print("Appuyez sur Ctrl+C pour arrêter le serveur proprement.")

    while True:
        client, addr = server.accept()
        print(f"Nouvelle connexion de {addr}")

        try:
            client.send(b"Bienvenue sur le serveur TCP! (Session ouverte)\n")

            while True:
                data = client.recv(1024)

                if not data:
                    break
                
                print(f"Reçu de {addr}: {data.decode('utf-8')}")

        except ConnectionResetError:
            print(f"Le client {addr} a coupé la connexion brutalement.")
        except Exception as e:
            print(f"Erreur lors de la communication avec {addr} : {e}")
        finally:
            print(f"Fermeture de la session pour {addr}")
            client.close()

except KeyboardInterrupt:
    print("\nArrêt du serveur (Ctrl+C).")
except Exception as e:
    print(f"Erreur fatale du serveur : {e}")
finally:
    server.close()
    print("Ressources libérées, serveur éteint.")