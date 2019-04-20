# Project 4 - TCPStringClientPersistent.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 7, 2019

# This program implements a TCP connection client

from socket import *

# starts the connection with the server
serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

while True:

    # asks the user to input a sentence and sends it to the server
    sentence = input("Input a lowercase sentence: ")
    clientSocket.send(sentence.encode())

    # if the client types quit, leaves the loop and closes the connection
    if sentence == "quit":
        clientSocket.close()
        break

    # Else, sends the sentence typed by the user to the server
    # and prints the modified sentence received from the server
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

# closes the connection socket after the user types quit

