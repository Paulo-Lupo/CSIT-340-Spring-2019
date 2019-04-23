# Project 5 - TCPMathServerPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the server side of a persistent TCP connection.
# It evaluates math expressions requests from clients.
# It can serve multiple clients. But if there is a client already using the server,
# new clients must wait until the old client is done using the server.

from socket import *

# creates a listening TCP socket
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

        # uses established TCP connection socket to receive an expression from a client
        expression = connectionSocket.recv(1024).decode()

        # closes the connection if the user types quit
        if expression == "quit":
            connectionSocket.close()
            print("Client connection closed: ", clientAddress)
            break

        # evaluates the input expression
        try:
            solution = str(eval(expression))

        except (SyntaxError, NameError):
            solution = "Invalid Input. Enter a valid input or type quit to quit"

        print(solution)

        # sends back the solution or error message
        connectionSocket.send(solution.encode())
