import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to host and port
client.connect(("127.0.0.1", 55555)) #same as the server

nickname = input("Choose a nickname: ")
# client has to send and receive

def receive():
    while True:
        try:
            # try to receive messages from server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occurred")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()