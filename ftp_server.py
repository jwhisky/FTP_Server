# server side
# CIS 457 Project 1
# Jessica Ricksgers Elijah Smith Sylas Agnew


#!/usr/bin/env python3

import socket
import select
import os
import signal
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4321        # Port to listen on (non-privileged ports are > 1023)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST, PORT))
    s.listen(1)
    print("Starting server on localhost port 4321")
    signal.signal(signal.SIGINT, signal_handler)

    while True:

        print("Waiting for someone to connect...")
        conn, client = s.accept()

        try:

            print("connected to: ", client)

            while True:

                data = conn.recv(1024)

                if (data.decode() == 'quit'):

                    conn.close()
                    socket.close()
                    print("Quitting!")
                    break

                else:

                    commands = data.decode().split(' ', 1)

                    if( len(commands) > 0):
                        
                        file = commands[1]

                    if (commands[0] == 'upload'):

                        with open(file, 'w') as writefile:

                            while True:
                                data = conn.recv(1024)

                                if not data:
                                    break

                                writefile.write(data.decode('utf-8'))
                                writefile.close()
                                break

                    elif (commands[0] == 'message'):

                        print(file)
                        conn.send(("recieved").encode())

                    elif (commands[0] == 'download'):

                        with open(file, 'r') as getfile:
                            for data in getfile:
                                conn.sendall(data.encode('utf-8'))

                    else:

                        conn.send(("Unknown command").encode())

        finally:

            print("Closing connection")
            conn.close()