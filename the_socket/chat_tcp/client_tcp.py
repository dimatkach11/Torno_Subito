import socket
import threading

nickname = input('Chose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ora dobbiamo collegare il client all'ip e porta del server
client.connect(('127.0.0.1', 15000))
def receive():
    while True:
        try:
            messagge = client.recv(1024).decode('ascii')
            if messagge == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(messagge)
        except:
            #print('\nAn error occurred!')
            client.close()
            break

def write():
    while True:
        try:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))
        except:
            #print('\nAn error occurred!')
            client.close()
            break


# ora serve un metodo che riceve sempre i dati dal server e alla stesso tempo un metodo che li invia e devono lavorare in simultanea, per questo avremmo bisogno dei Thread
receive_Thread = threading.Thread(target=receive)
receive_Thread.start()

write_Thread = threading.Thread(target=write)
write_Thread.start()