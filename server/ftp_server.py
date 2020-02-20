# server side
# CIS 457 Project 1
# Jessica Ricksgers Elijah Smith Silas Agnew


#!/usr/bin/env python3

import socket
import select
import os
import signal
import sys
import socket 
from _thread import *
import threading 
  
print_lock = threading.Lock() 

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4321         # Port to listen on (non-privileged ports are > 1023)

def threaded(conn): 

    while True:

        data = conn.recv(1024)
        print(str(conn.getsockname()) + ": " + str(data.decode()))

        if (data.decode() == 'quit'):

            #conn.close()
            #socket.close()
            print("Quitting!")
            break

        elif (data.decode() == 'list'):

            print("Sending Available Files to " + str(conn.getsockname()))
            conn.send('\n'.join(os.listdir(os.getcwd())).encode())

        else:

            commands = data.decode().split(' ', 1)

            if( len(commands) > 1):
                    
                filename = commands[1]

            if (commands[0] == 'send'):

                out = open(filename, 'wb')
                conn.send("size".encode())
                size = conn.recv(5)
                print(size.decode())
                size = int(size.decode())

                if (size > 0):

                    conn.send("send".encode())
                    written = 0
                    data = conn.recv(1024)
                    print("Receiving file...")
                    while True:
                        written += out.write(data)
                        if (written >= size):
                            break
                        data = conn.recv(1024)
                    print("Finished")

            elif (commands[0] == 'message'):

                print(filename)
                conn.send(("recieved").encode())

            elif (commands[0] == 'download'):
                # Protocol for sending is to send the size of the file upon
                # request then proceed to send file after client confirms size

                try:

                    size = os.path.getsize('./' + filename)
                    print("Size: " + str(size))
                    conn.send(str(size).encode()) # not dealing with byte conversion
                
                except:
                    conn.send('0'.encode())
                    continue

                confirm = conn.recv(1024)
                if (confirm.decode() == "download"):

                    with open(filename, 'rb') as getfile:
                        for data in getfile:
                            conn.sendall(data)

            else:

                conn.send(("Unknown command").encode())

    conn.close() 
    
  

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def Main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen(5)
        print("Starting server on localhost port " + str(PORT))
        signal.signal(signal.SIGINT, signal_handler)

        while True:

            print("Waiting for someone to connect...")
            conn, client = s.accept()

            print_lock.acquire()
            print("connected to: ", client)

            start_new_thread(threaded,(conn,))

        print("Closing connection")
        conn.close()

if __name__ == '__main__': 
    Main() 
