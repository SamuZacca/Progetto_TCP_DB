import socket
import facilities
HOST = '127.0.0.1'
PORT = 50006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data=s.recv(1024).decode()
print(data)
messaggio=str(input("Inserisci la password: "))
s.send(messaggio.encode())
data=s.recv(1024).decode()
while data=="Password errata!":
    print(data)
    messaggio=str(input("Reinserisci la password: "))
    s.send(messaggio.encode())
    data=s.recv(1024).decode()
print(data)
if data!="Hai terminato i tentativi a disposizione!":
    c_z=str(input("Scegli il database su cui vuoi lavorare (C=CLIENTI, Z=ZONA): "))
    while c_z!="C" and c_z!="Z":
        print("Database non valido!")
        c_z=str(input("Scegli il database su cui vuoi lavorare (C=CLIENTI, Z=ZONA): "))
    s.send(c_z.encode())
    azione=str(input("Scegli l'azione che vuoi fare (C=CREATE, R=READ, U=UPDATE, D=DELETE): "))
    while azione!="C" and azione!="R" and azione!="U" and azione!="D":
        print("Azione non valida!")
        azione=str(input("Scegli l'azione che vuoi fare (C=CREATE, R=READ, U=UPDATE, D=DELETE): "))
    s.send(azione.encode())
    if azione=="C":
        if c_z=="C":
            for i in range(0,6):
                risposta=s.recv(1024).decode()
                print(risposta)
                data=str(input(""))
                s.send(data.encode())
            risposta=s.recv(1024).decode()
            print(risposta)
        elif c_z=="Z":
            for i in range(0,4):
                risposta=s.recv(1024).decode()
                print(risposta)
                data=str(input(""))
                s.send(data.encode())
            risposta=s.recv(1024).decode()
            print(risposta)
    elif azione=="R":
        data=s.recv(1024)
        database=facilities.bytes_to_dict(data)
        print(database)
    elif azione=="U":
        if c_z=="C":
            for i in range(0,7):
                risposta=s.recv(1024).decode()
                print(risposta)
                data=str(input(""))
                s.send(data.encode())
            risposta=s.recv(1024).decode()
            print(risposta)
        elif c_z=="Z":
            for i in range(0,5):
                risposta=s.recv(1024).decode()
                print(risposta)
                data=str(input(""))
                s.send(data.encode())
            risposta=s.recv(1024).decode()
            print(risposta)
    elif azione=="D":
        risposta=s.recv(1024).decode()
        print(risposta)
        data=str(input(""))
        s.send(data.encode())
        risposta=s.recv(1024).decode()
        print(risposta)
print("Arrivederci Utente")
s.close()