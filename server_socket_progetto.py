import threading
import socket
import mysql.connector
import facilities
PASSWORD="zaccarelli1234"
def scrivi(s, diz):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    if s=="C":
        query1 = f"INSERT INTO clienti_samuele_zaccarelli(nome, cognome, data_nascita, luogo_nascita, posizione_lavorativa, data_assunzione) VALUES(\'{diz['Nome']}\', \'{diz['Cognome']}\', \'{diz['Data_Nascita']}\', \'{diz['Luogo_Nascita']}\', \'{diz['Posizione_Lavorativa']}\', \'{diz['Data_Assunzione']}\')"
        cur.execute(query1)
        conn.commit()
        return
    elif s=="Z":
        query2 = f"INSERT INTO zona_lavoro_samuele_zaccarelli(nome, numero_clienti, numero_dipendenti, id_dipendente) VALUES(\'{diz['Nome']}\', \'{diz['Numero_Clienti']}\', \'{diz['Numero_Dipendenti']}\', \'{diz['ID_Cliente']}\')"
        cur.execute(query2)
        conn.commit()
        return
def leggi(s):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    if s=="C":
        tot={}
        query1 = "SELECT * FROM clienti_samuele_zaccarelli"
        cur.execute(query1)
        dati1 = cur.fetchall()
        for i in range(0,len(dati1)):
            formato=dati1[i][3]
            Data_Nascita=formato.day,formato.month,formato.year
            formato=dati1[i][6]
            Data_Assunzione=formato.day,formato.month,formato.year
            clienti={'ID':dati1[i][0], 'Nome':dati1[i][1], 'Cognome':dati1[i][2], 'Data_Nascita':Data_Nascita, 'Luogo_Nascita':dati1[i][4], 'Posizione_Lavorativa':dati1[i][5], 'Data_Assunzione':Data_Assunzione}
            tot["Cliente"+str(i+1)]=clienti
        return tot
    elif s=="Z":
        tot={}
        query2 = "SELECT * FROM zona_lavoro_samuele_zaccarelli"
        cur.execute(query2)
        dati2 = cur.fetchall()
        for i in range(0,len(dati2)):
            zona={'ID':dati2[i][0], 'Nome':dati2[i][1], 'Numero_Clienti':dati2[i][2], 'Numero_Dipendenti':dati2[i][3], 'ID_Cliente':dati2[i][4]}
            tot["Zona"+str(i+1)]=zona
        return tot
def aggiorna(scelta, diz, ID):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    if scelta=="C":
        query1 = f"UPDATE clienti_samuele_zaccarelli SET Nome=\'{diz['Nome']}\', Cognome=\'{diz['Cognome']}\', Data_Nascita=\'{diz['Data_Nascita']}\', Luogo_Nascita=\'{diz['Luogo_Nascita']}\', Posizione_Lavorativa=\'{diz['Posizione_Lavorativa']}\', Data_Assunzione=\'{diz['Data_Assunzione']}\' WHERE ID=\'{ID}\'"
        cur.execute(query1)
        conn.commit()
        return
    elif scelta=="Z":
        query2 = f"UPDATE zona_lavoro_samuele_zaccarelli SET Nome=\'{diz['Nome']}\', Numero_Clienti=\'{diz['Numero_Clienti']}\', Numero_Dipendenti=\'{diz['Numero_Dipendenti']}\', ID_Cliente=\'{diz['ID_Cliente']}\' WHERE ID=\'{ID}\'"            
        cur.execute(query2)
        conn.commit()
        return
def elimina(s, data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    if s=="C":
        query1 = f"DELETE FROM clienti_samuele_zaccarelli where id=\'{data}\'"
        cur.execute(query1)
        conn.commit()
        return
    elif s=="Z":
        query2 = f"DELETE FROM zona_lavoro_samuele_zaccarelli where nome=\'{data}\'"
        cur.execute(query2)
        conn.commit()
        return
def gestisci_comunicazione(conn):
    try:
        while True:
            benvenuto=str("Benvenuto Utente!")
            conn.send(benvenuto.encode())
            data=conn.recv(1024).decode()
            for i in range(0,2):
                if data!=PASSWORD:
                    password=str("Password errata!")
                    conn.send(password.encode())
                    data=conn.recv(1024).decode()
                elif data==PASSWORD:
                    break
            if data!=PASSWORD:
                conn.send(("Hai terminato i tentativi a disposizione!").encode())
            elif data==PASSWORD:
                password=str("Password accettata!")
                conn.send(password.encode())
                scelta=conn.recv(1024).decode()
                if scelta=="C":
                    opzione=conn.recv(1024).decode()
                    if opzione=="C":
                        Nome=str("Inserisci il nome del cliente: ")
                        Cognome=str("Inserisci il cognome del cliente: ")
                        Data_Nascita=str("Inserisci la data di nascita del cliente (Anno-Mese-Giorno): ")
                        Luogo_Nascita=str("Inserisci il luogo di nascita del cliente: ")
                        Posizione_Lavorativa=str("Inserisci la posizione lavorativa del cliente: ")
                        Data_Assunzione=str("Inserisci la data di assunzione del cliente: ")
                        conn.send(Nome.encode())
                        Nome=conn.recv(1024).decode()
                        conn.send(Cognome.encode())
                        Cognome=conn.recv(1024).decode()
                        conn.send(Data_Nascita.encode())
                        Data_Nascita=conn.recv(1024).decode()
                        conn.send(Luogo_Nascita.encode())
                        Luogo_Nascita=conn.recv(1024).decode()
                        conn.send(Posizione_Lavorativa.encode())
                        Posizione_Lavorativa=conn.recv(1024).decode()
                        conn.send(Data_Assunzione.encode())
                        Data_Assunzione=conn.recv(1024).decode()
                        clienti={'Nome':Nome, 'Cognome':Cognome, 'Data_Nascita':Data_Nascita, 'Luogo_Nascita':Luogo_Nascita, 'Posizione_Lavorativa':Posizione_Lavorativa, 'Data_Assunzione':Data_Assunzione}
                        scrivi(scelta, clienti)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
                    elif opzione=="R":
                        clienti=leggi(scelta)
                        clienti=facilities.dict_to_bytes(clienti)
                        conn.send(clienti)
                    elif opzione=="U":
                        ID=str("Inserisci il l'ID del cliente da modificare: ")
                        Nome=str("Inserisci il nome del cliente: ")
                        Cognome=str("Inserisci il cognome del cliente: ")
                        Data_Nascita=str("Inserisci la data di nascita del cliente (Anno-Mese-Giorno): ")
                        Luogo_Nascita=str("Inserisci il luogo di nascita del cliente: ")
                        Posizione_Lavorativa=str("Inserisci la posizione lavorativa del cliente: ")
                        Data_Assunzione=str("Inserisci la data di assunzione del cliente: ")
                        conn.send(ID.encode())
                        ID=conn.recv(1024).decode()
                        conn.send(Nome.encode())
                        Nome=conn.recv(1024).decode()
                        conn.send(Cognome.encode())
                        Cognome=conn.recv(1024).decode()
                        conn.send(Data_Nascita.encode())
                        Data_Nascita=conn.recv(1024).decode()
                        conn.send(Luogo_Nascita.encode())
                        Luogo_Nascita=conn.recv(1024).decode()
                        conn.send(Posizione_Lavorativa.encode())
                        Posizione_Lavorativa=conn.recv(1024).decode()
                        conn.send(Data_Assunzione.encode())
                        Data_Assunzione=conn.recv(1024).decode()
                        clienti={'Nome':Nome, 'Cognome':Cognome, 'Data_Nascita':Data_Nascita, 'Luogo_Nascita':Luogo_Nascita, 'Posizione_Lavorativa':Posizione_Lavorativa, 'Data_Assunzione':Data_Assunzione}
                        aggiorna(scelta, clienti, ID)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
                    elif opzione=="D":
                        ID=str("Inserisci l'ID dell'utente da eliminare: ")
                        conn.send(ID.encode())
                        data=conn.recv(1024).decode()
                        elimina(scelta, data)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
                elif scelta=="Z":
                    opzione=conn.recv(1024).decode()
                    if opzione=="C":
                        Nome=str("Inserisci il nome della zona: ")
                        Numero_Clienti=str("Inserisci il numero di clienti nella zona: ")
                        Numero_Dipendenti=str("Inserisci il numero di dipendenti della zona: ")
                        ID_Cliente=str("Inserisci l'ID del cliente: ")
                        conn.send(Nome.encode())
                        Nome=conn.recv(1024).decode()
                        conn.send(Numero_Clienti.encode())
                        Numero_Clienti=conn.recv(1024).decode()
                        conn.send(Numero_Dipendenti.encode())
                        Numero_Dipendenti=conn.recv(1024).decode()
                        conn.send(ID_Cliente.encode())
                        ID_Cliente=conn.recv(1024).decode()
                        zona={'Nome':Nome, 'Numero_Clienti':Numero_Clienti, 'Numero_Dipendenti':Numero_Dipendenti, 'ID_Cliente':ID_Cliente}
                        scrivi(scelta, zona)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
                    elif opzione=="R":
                        zona=leggi(scelta)
                        zona=facilities.dict_to_bytes(zona)
                        conn.send(zona)
                    elif opzione=="U":
                        ID=str("Inserisci il l'ID del reparto da modificare: ")
                        Nome=str("Inserisci il nome della zona: ")
                        Numero_Clienti=str("Inserisci il numero di clienti nella zona: ")
                        Numero_Dipendenti=str("Inserisci il numero di dipendenti della zona: ")
                        ID_Cliente=str("Inserisci l'ID del cliente: ")
                        conn.send(ID.encode())
                        ID=conn.recv(1024).decode()
                        conn.send(Nome.encode())
                        Nome=conn.recv(1024).decode()
                        conn.send(Numero_Clienti.encode())
                        Numero_Clienti=conn.recv(1024).decode()
                        conn.send(Numero_Dipendenti.encode())
                        Numero_Dipendenti=conn.recv(1024).decode()
                        conn.send(ID_Cliente.encode())
                        ID_Cliente=conn.recv(1024).decode()
                        zona={'Nome':Nome, 'Numero_Clienti':Numero_Clienti, 'Numero_Dipendenti':Numero_Dipendenti, 'ID_Cliente':ID_Cliente}
                        aggiorna(scelta, zona, ID)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
                    elif opzione=="D":
                        Nome=str("Inserisci il nome della zona da eliminare: ")
                        conn.send(Nome.encode())
                        data=conn.recv(1024).decode()
                        elimina(scelta, data)
                        risposta=str("Operazione riuscita!")
                        conn.send(risposta.encode())
    except:
        pass    
print("Server in ascolto: ")
HOST = ''
PORT = 50006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
i=0
lista_connessioni = []
while True:
    lista_connessioni.append( s.accept() ) 
    print(lista_connessioni[i][1], "si è connesso!")
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1