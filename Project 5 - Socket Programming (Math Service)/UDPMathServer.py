# Project 5 - UDPMathServer.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the server side of a UDP connection
# It evaluates math expressions requests from clients

from socket import *

# creates a UDP socket
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")

while True:
    # receives the expression from a client through the socket
    expression, clientAddress = serverSocket.recvfrom(2048)
    print("New client request from: ", clientAddress)

    # evaluates the given expression
    try:
        solution = str(eval(expression))

    except (SyntaxError, NameError):
        solution = "Invalid Input. Enter a valid input or type quit to quit"

    print(solution)

    # sends back the solution or error message
    serverSocket.sendto(solution.encode(), clientAddress)

serverSocket.close()
print("Client connection closed: ", clientAddress)
