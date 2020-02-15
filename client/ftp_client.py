#client side
#CIS 457 Project 1
#Jessica Ricksgers Elijah Smith Silas Agnew

#!/usr/bin/env python3

import socket
import selectors

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4321        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

def connect(serverPort):
    try:
        print(' Connecting...')

        serverAddress = (HOST, int(serverPort))
        s.connect(serverAddress)

        print(' Connected!')

    except:
        print(' ERROR - Could NOT connect to server!')
        return False

    return True

while True:

    mes = input("Enter your command: ")

    if (mes == 'connect'):

        address = input('please enter port number: ')
        connected = connect(address)

    if (mes == 'list'):
        
        if (not connected):
            
            print("Connect to server first!")
            continue

        s.send(mes.encode())
        print("Files:")
        data = s.recv(1024)
        print(data.decode())

    if (mes.startswith('retrieve')):

        if (not connected):
            
            print("Connect to server first!")
            continue

        tokens = mes.split(' ')
        if (len(tokens) < 2):

            print("Bad format. Proper usage: retrieve <filename>")
            continue
        
        out = open(tokens[1], 'wb')
        s.send(('download ' + tokens[1]).encode())

        print("Downloading " + tokens[1] + "...");

        kilo = s.recv(1024)
        while kilo:
            out.write(kilo)
            kilo = s.recv(1024)
        out.close()

        print("Finished")

    if (mes == 'quit'):

        print('Quitting!')
        break
    
    if (mes == 'message'):

        x = input('enter message to send to server:')
        s.send(x.encode())
        #data = s.recv(1024)
        #print('Received', repr(data))


