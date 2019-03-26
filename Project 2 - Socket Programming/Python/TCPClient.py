# Project 2 - TCPCliet.py			
# Student Name: Joao Paulo D. S. Ferreira	
# CSIT 340-01 - Computer Networks 		
# Dr. Dawei Li		
# March 14, 2019				

# This program implements a non-persistent 
# TCP connection from the client side
# by using Socket Programming

from socket import *

# starts the connection with the server
serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

sentence = input("Input a lowercase sentece: ")

# continues sending requests until the user types Quit
while(sentence != "Quit"):

    # Sends the sentence typed by the user to the server
    # and prints the modified sentence recieve from the server
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
    clientSocket.close()

    # Since the server is using a non-persistent implemenation
    # we must start a new socket connection for each request
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    sentence = input("Input a lowercase sentece: ")

# closes the connection after the user types Quit
clientSocket.close()
