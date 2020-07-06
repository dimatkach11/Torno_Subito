#
# ! FTP : File Transfer Protocol
# * In computing and telecomunications, is a protocol for data trasmission between hosts based on TCP and with client-server architecture.
# * The protocol uses separate TCP connections to transfer data and to control transfers and requires client authentication via username and password, althrough the server can be configured for anonymous connections with fictitious credentials. 
# * Since FTP transmits both this credentials and any other comunication in plain text, and since it has no server authentication mechanisms at the client, the protocol is often made secure using an SSL/TLS sublayer and this variant is called FTPS.
# * L'acronimo SFTP indica invece un altro protocollo che, sebbene molto simile a quest'ultimo da un punto di vista funzionale, è piuttosto diverso da quello tecnologico: SSH File Transfer Protocol.
# * FTP, a differenza di altri protocolli come HTTP, utilizza due connessioni separate per gestire comandi e dati.
# * Un server FTP generalmente ascolta sulla porta 21 TCP a cui si connette il client. La connessione da parte del client determina l'inizializzazione del canale di comando attraverso il quale client e server scambiano comandi e risposte.
# * L'effettivo scambio di dati (come un file) richiede l'apertura del canale dati, che può essere di due tipi.
# * In un canale di dati di tipo attivo, il client apre una porta che di solito è casuale; attraverso il canale di comando, il client rivela il numero di quella porta al server e attende che si connetta.
# * Una volta che il server ha attivato la connessione dati al client FTP, il client associa la porta di origine alla porta 20 del server FTP. I comandi PORT o EPRT possono essere utilizzati a questo scopo, a seconda del protocollo di rete utilizzato (di solito IPv4 o IPv6).
# * Sia il canale di comando che il canale dati sono connessioni TCP; FTP crea un nuovo canale dati per ciascun file trasferito all'interno della sessione utente, mentre il canale di comando rimane aperto per l'intera durata della sessione utente, in altre parole il canale di comando è persistente mentre il canale di dati non è persistente.
# * Un server FTP offre diverse funzioni che consentono al client di interagire con il suo filesystem e i file che lo popolano, tra cui:

# * Scarica / carica file.

# * Riprendi i trasferimenti interrotti.

# * Rimozione e ridenominazione dei file.

# * Creazione directory.

# * Navigazione nella directory.

# * FTP fornisce anche un'autenticazione chiara (non crittografata) degli accessi. Potrebbe essere necessario che il client che si connette fornisca le credenziali in base alle quali verranno assegnati determinati privilegi per operare sul filesystem. La cosiddetta autenticazione "anonima" richiede che il client non specifichi alcuna password di accesso e che il client disponga di privilegi generalmente "di sola lettura".


import ftplib

def ftp_connect():
    while True:
        address = input('Please enter ftp address or digit \'exit\' to close application: ') 
        if address == 'exit':
            break
        else:
            pass
        #address = 'ftp.acc.umu.se'
        print('connecting...')
        try: 
            with ftplib.FTP(address) as ftp:
                ftp.login()
                print(ftp.getwelcome())
                print('Current Directory', ftp.pwd())
                ftp.dir()
                print('Valid comands are cd/get/ls/exit -> ex: get readme.txt')
                ftp_comand(ftp)
                break # once ftp comand() exits, end this function (exit program)
        except ftplib.all_errors as e:
            print('Failed to connect, check your address and credentials.', e)



def ftp_comand(ftp):
    while True: # run until 'exit' comand received from user
        comand = input('Enter a comand: ')
        comands = comand.split() # split comand and file/directory into list

        if comands[0] == 'cd': # change directory
            try:
                ftp.cwd(comands[1])
                print('Directory of', ftp.pwd())
                ftp.dir()
                print('Crrent Directory', ftp.pwd())
            except ftplib.error_perm as e: # Handle 550 (not found / no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'Directory may not exist or you may not have permission to view it.')

        elif comands[0] == 'get': # download file
            try:
                ftp.retrbinary(f'RETR {comands[1]}', open(f'FTP/download_files/{comands[1]}', 'wb').write)
                print('File successfully downloaded')
            except ftplib.error_perm as e: # Handle 550 (not found / no permission error)
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'File may not exist or you may not have permission to downloaded it.')

        elif comands[0] == 'ls': #  Print directory listing
            print('Directory of', ftp.pwd())
            ftp.dir()
            print('Crrent Directory', ftp.pwd())

        elif comands[0] == 'exit': #  Exit application
            ftp.quit()
            print('Good bye')
            break

        else: 
            print('Invalid command, try again (valid options: cd/get/ls/exit -> ex: get readme.txt')

print('\n\t\t\t\t\t\tWelcome to Python FTP\n')
ftp_connect()



# ! Approfondimenti su FTP:
# Protocollo tra i più vecchi inventato nel 1971 ancor prima dei protocolli TCP/IP. La versione su FTP su TCP/IP e nata nel 1980 
# Oggi le compagnie di hosting spesso utilizzano questo protocollo per caricare i file sul web server, server che poi utilizzeranno il protocollo HTTP per trasmettere i dati.
# * Comandi FTP:
# USER : mostra il nome del utente
# PASS : mostra la password
# LIST : mostra l'elenco della directory
# CWD : cambio directory
# RETR : trasferire file dal server al client -> comando analogo su POP3 esiste
# STOR : trasferire file dal client al server
# TYPE : tipo di trasferimento -> text o binary
# DELE : cancellare un file
# MKD : creare una directory
# RMD : eliminare una directory
# PASV : utilizzare un regime passivo -> di default il regime è attivo
# QUIT : uscire ed interrompere la connessione