# Project 2 - UDPServer.py			
# Student Name: Joao Paulo D. S. Ferreira	
# CSIT 340-01 - Computer Networks 		
# Dr. Dawei Li		
# March 14, 2019				

# This program implements a UDP connection
# from the server side by using Socket Programming

from socket import *

# opens the server for requests
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")
while True:

        # recieves the message sent with the request and modifies it
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        print("message to be sent back: ")
        print(modifiedMessage)

        # Sends back the modified message to the client
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
