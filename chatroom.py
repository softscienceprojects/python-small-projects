"""
TCP chat room
create server - multiple clients can send messages to server
this is the server file
"""

import socket
import threading

# define host address and port for server

host = '127.0.0.1' # localhost - our machine. if on web server, use ip address of web server
port = 55555 # dont take ports like 80 or well-known ports (1-1000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#bind server to host & ip
server.bind((host, port)) #server bound to port on localhost
server.listen() #listening for incoming connections

#broadcast, handle, receive methods

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message) #broadcast to server 

# receive message from client - and send back to all other clients

def handle(client):
    while True:
        try:
            # try to receive message from client. if succeeds, send to everyone else
            message = client.recv(1024) #bytes 
            broadcast(message)
        except:
            # terminate this loop
            index = clients.index(client) #where is this client i nthe list?
            clients.remove(client)
            client.close()
            nickname = nicknames[index] #also remove their nickname
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        #server accepts all connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send("connected to the server".encode('ascii'))
        #one thread for each client - process at roughly same time
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is listening...")
receive()