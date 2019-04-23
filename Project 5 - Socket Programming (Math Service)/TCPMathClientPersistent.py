# Project 5 - TCPMathClientPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the client side of a persistent TCP connection.
# It evaluates math expressions requests from clients.
# It can serve multiple clients, but if there is a client already using the server,
# new clients must wait until the old client is done using the server.

from socket import *

# starts the connection with the server
serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:

    # gets a math expression as an input string
    expression = input("Input a basic expression: ")

    # sends the expression to the server
    clientSocket.send(expression.encode())

    # if the client types quit, leaves the loop, which will close the connection
    if expression == "quit":
        break

    # receives the solution from the server
    solution = clientSocket.recv(1024)

    # prints the solution as a string
    print(solution.decode())

# closes the connection socket after the user has typed quit
clientSocket.close()
