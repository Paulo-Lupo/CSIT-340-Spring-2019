# Project 4 - TCPStringServerPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 7, 2019

# This program implements a persistent TCP connection server

from socket import *

# opens the server allowing it to queue 2 connections at a time
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print("The server is ready to receive.")


while True:
    # accepts connections coming through the server socket
    connectionSocket, clientAddress = serverSocket.accept()
    print("New client connection: ", clientAddress)

    while True:
        # receives a string from the client
        sentence = connectionSocket.recv(1024).decode()

        # closes the connection socket if the client types quit
        if sentence == "quit":
            print("Client connection closed: ", clientAddress)
            connectionSocket.close()
            break

        # changes the message received from the connection and sends it back
        capitalizedSentence = sentence.upper()
        print(capitalizedSentence)
        connectionSocket.send(capitalizedSentence.encode())
