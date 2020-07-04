import threading
import socket

host = '127.0.0.1' 
port = 15000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# funzione che manda il messaggio a tutti i clienti connessi tranne che al client che manda tali messaggi
def broadcast(client, messagge):
    for generic_client in clients:
        if generic_client != client:
            generic_client.send(messagge)

# per il cliente che si collega il server ricevera i messaggi da lui e li manderà a tutti i clienti connessi
# quando un cliente si collega il servere cercherà di ricevre i messaggi da tali clienti, se il cliente non invierà niente non succede niente, ma se il client esce si genererà un errore, raise an exception, allora rimuovere il client dalla lista e lo diremmo a tutti gli altri client attraverso la funzione broadcast e infine rimuoveremo anche il suo nickname.
def handle(client, address):
    while True:
        try:
            messagge = client.recv(1024)
            broadcast(client, messagge)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            print(f'\n{str(address)} <== Left chat room') 
            print(f'\n\t\tClients now connected are --> {len(clients)} ')
            nickname = nicknames[index]
            broadcast(client, f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# metodo principale che combina tutto
def receive():
    while True:
        # qui accettiamo i clienti nuovi tutto il tempo
        client, address = server.accept()
        print(f'\n{str(address)} ==> Join chat room') # prendiamo i loro indirizzi

        # Ora vogliamo chiedere al client il suo nickname inviandoli un messaggio
        client.send('NICK'.encode('ascii'))
        # E attendiamo adesso la risposta dal client
        nickname = client.recv(1024).decode('ascii')
        # ora possiamo inserire il nickname il client nelle correspettive liste
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}! ')
        print(f'\n\t\tClients now connected are --> {len(clients)} ')
        #ora facciamo sapere a tutti i clienti connessi che un nuovo cliente si ecollegato con il nickname
        broadcast(client, f'{nickname} joined the chat! '.encode('ascii'))
        # e allo specifico client diciamo 
        client.send('Connected to the server!'.encode('ascii'))

        # ora dobbiamo assegnare un thread per ogni client che si collega, in modo che possono inviare i messaggi nello stesso tempo in modo indipendente
        thread = threading.Thread(target=handle, args=(client, address))
        thread.start()

# * Faccio partire il metodo principale che lega il resto
print('\nServer is listening...')
print(f'\n\t\tClients now connected are --> {len(clients)} ')
receive()