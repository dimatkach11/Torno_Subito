#
# ! Obiettivi :
# * 1 -> Ricevere una richiesta dal cliente
# * 2 -> Leggere la richiesta, e capire cosa vuole
# * 3 -> Capire che metodo utilizza
# * 4 -> Capire che pagina cerca
# * 5 -> In base alla richiestà generare una risposta

# Si lavorerà con il protocollo http bastao su altri due protocolli, tcp , ip
# * http
# * tcp --> trasmission controll protocol --> port
# porta ordine nel caos generato dal protocollo ip tenendo conto dell'ordine tra invio e ricevimento dei pacchetti scambiati tra host. Se manca un pacchetto fa una richiesta ripetuta al mandante, se riceve dei duplicati li scarta. La sua particolarità è nel fatto che aggiunge la porta allo scambio di dati. La porta serve affinche più macchine possano utilizzare il tunnel tcp sennza occuparlo completamente. 
# * ip --> ip address 
# da solo può causare la perdita di dati tra due host
# * coppia -->  ip address: port = socket
# socket è una presa e serve da collegamento tra un server e un client. per questo esistono due tipi di socket: server e client. 

import socket 
from views import *



def run():
    # * qui stiamo difenedo il socket dalla parte del server che ascolta ed elabora
    # ricevimento pacchetti attraverso questi protocolli: ip, tcp
    #creazione presa server      # * AF_INET <=> ip; SOCK_STREAM <=> tcp
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # extra settaggi: SOL_SOCKET ->SOL = socket level e ci serve il socket nostro del server -> _SOCKET, il secondo parametro che mettiamo SO = socket optiot _REUSEADDR per riutilizzare l'indirizzo, e mettiamo tutto in True con 1
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bisogna legare la presa con un inidirizzo e porta
    server_socket.bind(('localhost', 15000))
    # ora bisogna controllare se sono stati inviati pacchetti su tale inidirizzo e porta. Bisogna mettere il server in ascolto su tale porta.
    server_socket.listen()
    # non sapendo quanto sarà lungo tale scambio di dati tra i clienti e il server bisogna utilizzare un cilclo infinito, dove tali richieste andranno analizzati ed elaborati per generare le risposte in base alle richieste.
    while True:
        # Ora bisogna ricevere dati inviati dai clienti:
        # il seguente metodo accept() del socket server ritorna due elementi, il (socket, indirizzo) del cliente che sta facendo la richiesta al nostro server
        client_socket, addr = server_socket.accept()
        # client_socket è chi invia la richiestà dal parte del client, addr è il suo indirizzo che avrà una porta diversa, assegnata dal sistema.
        # ora bisogna vedere cosa sta inviando il client_socket:
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)

        # * Ora bisogna rispondere al cliente
        response = generate_response(request.decode())
        client_socket.sendall(response)
        # non vedremmo niente nel browser fin che non chiudiamo il collegamento.
        client_socket.close()

# funzione che estrae dati dalla richiesta inviata al server dal nostro client (browser) 
def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)

# funzione che genererà la risposta da inviare al browser (client)
def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (headers + body).encode()

def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    
    return URLS[url]()

def generate_headers(method, url):
    if not method == 'GET':
        return('HTTP/1.1 405 Method not allowed\n\n', 405)

    if url not in URLS:
        return('HTTP/1.1 404 Not found\n\n', 404)

    return('HTTP/1.1 200 \n\n', 200)

URLS = {
    '/': index,
    '/blog': blog
}

if __name__ == "__main__":
    run()




























#import socket
#from views import *

#URLS = {
#    '/' : index,
#    '/blog': blog
#}

#def parse_request(request):
#    parsed = request.split(' ')
#    method = parsed[0]
#    url = parsed[1]
#    return (method, url)

#def generate_headers(method, url):
#    if not method == 'GET':
#        return ('HTTP/1.1 405 Method not allowed\n\n', 405)
    
#    if not url in URLS:
#        return ('HTTP/1.1 404 Not found\n\n', 404)

#    return ('HTTP/1.1 200 ok\n\n', 200)

#def generate_content(code, url):
#    if code == 404:
#        return '<h1>404</><p>Not found</p>'  
#    if code == 405:
