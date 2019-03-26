# Project 2 - UDPCliet.py			
# Student Name: Joao Paulo D. S. Ferreira	
# CSIT 340-01 - Computer Networks 		
# Dr. Dawei Li		
# March 14, 2019				

# This program implements a UDP connection
# from the client side by using Socket Programming

from socket import *

# starts the connection with the server
serverHost = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input a lowercase sentece: ")

# Continues sending requests until the user types Quit
while(message != "Quit"):
    
    # Sends the sentence typed by the user to the server
    # and prints the modified sentence recieve from the server
    clientSocket.sendto(message.encode(), (serverHost, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    message = input("Input a lowercase sentece: ")

# closes the connection after the user types Quit 
clientSocket.close()
