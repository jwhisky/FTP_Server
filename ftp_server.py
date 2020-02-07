#server side
#CIS 457 Project 1
#Jessica Ricksgers Elijah Smith Sylas Agnew


#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# allows a client to connect to a server
def CONNECT(address, port):

# When this command is sent to the server, the server returns a list of 
# the files in the current directory on which it is executing.
# The client should get the list and display it on the screen.
def LIST():

# This command allows a client to get a file specified by
# its filename from the server.
def RETRIEVE(filename):

# This command allows a client to send a file specified
# by its filename to the server.
def STORE(filename):

# This command allows a client to terminate the control connection.
# On receiving this command, the client should send it to the server
# and terminate the connection. When the ftp_server receives the quit
# command it should close its end of the connection.
def QUIT():

