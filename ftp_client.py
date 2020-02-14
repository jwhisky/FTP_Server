#client side
#CIS 457 Project 1
#Jessica Ricksgers Elijah Smith Sylas Agnew

#!/usr/bin/env python3

import socket
import selectors

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4321        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(serverPort):
    try:
        print(' Connecting...')

        serverAddress = (HOST, int(serverPort))
        s.connect(serverAddress)

        print(' Connected!')

    except:
        print(' ERROR - Could NOT connect to server!')

while True:

    mes = input("Enter your command: ")

    if (mes == 'connect'):

        address = input('please enter port number: ')
        connect(address)


    if (mes == 'quit'):

        print('Quitting!')
        break
    
    if (mes == 'message'):

        x = input('enter message to send to server:')
        s.send(x.encode())
        #data = s.recv(1024)
        #print('Received', repr(data))


