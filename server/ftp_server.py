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

        while True:

            data = conn.recv(1024)
            print(str(conn.getsockname()) + ": " + str(data.decode()))

            if (data.decode() == 'quit'):

                conn.close()
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

                    with open(filename, 'wb') as writefile:

                        k = conn.recv(1024)
                        while (k):
                            writefile.write(k)
                            k = conn.recv(1024)
                        
                elif (commands[0] == 'message'):

                    print(filename)
                    conn.send(("recieved").encode())

                elif (commands[0] == 'download'):

                    with open(filename, 'r') as getfile:
                        for data in getfile:
                            conn.sendall(data.encode('utf-8'))
                    conn.shutdown(socket.SHUT_WR)

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
