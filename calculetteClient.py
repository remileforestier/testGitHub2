import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
msg_recu = connexion_avec_serveur.recv(1024)

if msg_recu == b"Hello from Serveur":
    print(msg_recu)
    msg_a_envoyer = b"Hello from Client"
    connexion_avec_serveur.send(msg_a_envoyer)

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("""What do you want to do? \n 
                          \t- ADDITION\n
                          \t- SOUSTRACTION\n
                           \t- MULTIPLICATION\n
                           \t-DIVISION\n
                           \t-QUIT\n""")
    try:
        assert msg_a_envoyer.upper() == ('ADDITION' or 'SOUSTRACTION' or 'MULTIPLICATION' or 'DIVISION' or 'QUIT')
        msg_a_envoyer = msg_a_envoyer.encode()
        connexion_avec_serveur.send(msg_a_envoyer.upper())
        msg_recu = connexion_avec_serveur.recv(1024)

    except:
        print("Ask for a valid operation ('ADDITION' or 'SOUSTRACTION' or 'MULTIPLICATION' or 'DIVISION' or 'QUIT')")

    try:
        s1 = input(msg_recu.decode())# Là encore, peut planter s'il y a des accents
        #print('tutto ben')
        s1 = s1.encode()
        print(s1)
        connexion_avec_serveur.send(s1)
        msg_recu = connexion_avec_serveur.recv(1024)


    except Exception as e:

        print(e)
        print("Should be a float")

    try:
        s2 = input(msg_recu.decode())# Là encore, peut planter s'il y a des accents            connexion_avec_serveur.send(s2)
        s2 = s2.encode()
        print(s2)
        connexion_avec_serveur.send(s2)
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu)

    except Exception as e:
        print(e)
        print("Should be a float")


print("Fermeture de la connexion")
connexion_avec_serveur.close()