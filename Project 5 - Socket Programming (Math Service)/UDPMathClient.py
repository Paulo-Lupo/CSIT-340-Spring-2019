# Project 5 - UDPMathClient.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements the client side of a UDP connection
# It sends math expressions to a server and prints the solution
# received as a response from the server

from socket import *

# starts the socket connection with the server
serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# gets the math expression as an input string
expression = input("Input a basic expression: ")

# Continues sending requests until the user types quit
while expression != "quit":
    
    # sends the expression typed by the user to the server
    clientSocket.sendto(expression.encode(), (serverHost, serverPort))

    # prints the solution received from the server
    solution, serverAddress = clientSocket.recvfrom(2048)
    print(solution.decode())

    # gets another math expression from the user
    expression = input("Input a basic expression: ")

# closes the connection after the user types quit
clientSocket.close()
