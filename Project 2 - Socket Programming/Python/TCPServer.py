# Project 2 - TCPServer.py			
# Student Name: Joao Paulo D. S. Ferreira	
# CSIT 340-01 - Computer Networks 		
# Dr. Dawei Li		
# March 14, 2019				

# This program implements a non-persistent 
# TCP connection from the server side
# by using Socket Programming

from socket import *

# opens the server
# allowing it to listen to 1 connection at a time
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

# keeps the connection open until the process is killed
while True:

    # accepts the connection coming through the server socket
    connectionSocket, addr = serverSocket.accept()    
    sentence  = connectionSocket.recv(1024).decode()

    # changes the message recieve from the connection
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence)

    # sends the modified message back and closes the connection
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
