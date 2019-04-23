# Project 5 - TCPMathClientNonPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the client side of a non-persistent TCP connection.
# It evaluates math expressions requests from clients.
# It can serve multiple clients.

from socket import *

# defines the host address and port #
serverHost = 'localhost'
serverPort = 5000

# gets the math expression as an input string
expression = input("Input a basic expression: ")

# continues sending requests until the user types quit
while expression != "quit":

    # connects to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))

    # uses newly created TCP connection to send an expression to the server
    clientSocket.send(expression.encode())

    # receives the solution from the server through the TCP connection socket
    solution = clientSocket.recv(1024)

    # prints the solution as a string
    print(solution.decode())

    # closes the TCP connection socket
    clientSocket.close()

    # gets another math expression as an input string
    expression = input("Input a basic expression: ")
