# 
# ! POP : Post Office Protocol
# * Is a client-server apllication layer protocol that has the task of allowing, through authentification, access by the client to an-email account on a host server and download the e-mails of the account itself.
# * POP(in version 3) waits on port 110 of the host(by default, but may be different) for a TCP connection from a client.
# * port 993 if you want to connect using POP3 securely (SSL)

import poplib

# * Scarica tutte le email 
#box = poplib.POP3_SSL('pop.gmail.com', 995)
#box.user('dimitritkach@gmail.com')
##box.pass_('') # todo da inserire la password
#N = len(box.list()[1])
#for i in range(N):
#    for msg in box.retr(i+1)[1]:
#        print(msg)
#box.quit()


# * Scarica ultimo messaggio ricevuto
import getpass

server = 'pop.gmail.com'

server_box = poplib.POP3_SSL(server, 995)
server_box.user('dimitritkach@gmail.com')

pwd = getpass.getpass(prompt='Inserisci password gmail: ')
server_box.pass_(pwd)

num_me = len(server_box.list()[1])
print('')

print(f'messaggi presenti nella mailbox {num_me}')
print('ultimo messaggio ricevuto:')
print(server_box.retr(num_me)[1])
server_box.quit()