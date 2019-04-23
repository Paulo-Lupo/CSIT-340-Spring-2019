# Project 5 - TCPMathServerNonPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the server side of a non-persistent TCP connection.
# It evaluates math expressions requests from clients.
# It can serve multiple clients.

from socket import *

# creates a listening TCP socket
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

while True:

    # waits from a request from the client
    connectionSocket, clientAddress = serverSocket.accept()
    print("New client request from: ", clientAddress)

    # uses established TCP connection socket to receive an expression from a client
    expression = connectionSocket.recv(1024).decode()

    # evaluates the given expression
    try:
        solution = str(eval(expression))

    except (SyntaxError, NameError):
        solution = "Invalid Input. Enter a valid input or type quit to quit"

    print(solution)

    # sends solution back and closes the connection
    connectionSocket.send(solution.encode())
    connectionSocket.close()
    print("Client connection closed: ", clientAddress)
