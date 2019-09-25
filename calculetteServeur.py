import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()
connexion_avec_client.send(b"Hello from Serveur")


msg_recu = b""

while msg_recu != b"QUIT":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever un exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())

    if msg_recu.decode() == 'ADDITION':
        connexion_avec_client.send(b"What is the first number you want to add")
        s1 = float(connexion_avec_client.recv(1024).decode())
        print('First number is received')
        connexion_avec_client.send(b"What is the second number you want to add")
        s2 = float(connexion_avec_client.recv(1024))
        print('Second number is received')
        connexion_avec_client.send("The result of your addition is {}".format(s1+s2))

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()