#client side
#CIS 457 Project 1
#Jessica Ricksgers Elijah Smith Sylas Agnew

#!/usr/bin/env python3

import socket
import selectors

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4321        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        mes = input("Enter your command: ")

        if (mes == 'quit'):

            print('Quitting!')
            break
        

        s.send(mes.encode())
        data = s.recv(1024)
        print('Received', repr(data))

    s.close()

