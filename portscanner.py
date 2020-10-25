""" 
find an open port - unnec. open port might be a security gap
for penetration testing. ILLEGAL if you don't have permission!
Just for your own computer/server. 

"""

import socket
import threading
from queue import Queue

target = '127.0.0.1' #ip address. can test on your router. 127.0.0.1 = localhost
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket is an internet socket, tcp instead of usp
        sock.connect((target, port)) #target ip address and the port
        return True #port scan successful = open
    except:
        return False

# too slow
# for port in range(1, 1024):
#     result = portscan(port)
#     if result:
#         print("Port {} open".format(port))
#     else:
#         print("Port {} is closed".format(port))

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(10): #10 threads
    thread = threading.Thread(target=worker) #referring to worker function without calling it
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

#wait for all threads to finish
for thread in thread_list:
    thread.join() #wait until thread is odne until you continue

print("Open port are: {}".format(open_ports))
