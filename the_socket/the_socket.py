#
# ! SOCKET
# * is a way of connecting two nodes on a network to communicate with each other.


# * Connect a host to the google services:
import socket
import sys

# made a socket 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket sucessfully created')
except socket.error as err:
    print(f'socket creation failed with error {err}')

# default port for socket
port = 80

# resolved google's ip
try:
    host_ip = socket.gethostbyname('www.google.com')
    #print(host_ip)
except socket.gaierror:
    # this means could not resolve the host
    print('there was an error resolving the host')
    sys.exit()

# connecting to the server --> google
s.connect((host_ip,port))

print(f'The socket has successfully connected to google on: \nhost_ip ==> {host_ip} \nport ==> {port} ')

# now we need to know how can we send some data through a socket
# for this a socket library has a sendall function, wich allows you to send data to a server to which the socket is connected and server can also send data to the client using this function.


