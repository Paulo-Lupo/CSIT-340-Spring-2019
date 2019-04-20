# Project 4 - TCPStringServerPersistentMultithread.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 7, 2019

# This program implements a persistent TCP connection server
# It uses multithreading to allow clients to use the server simultaneously

from socket import *
import threading


# defines the task to be executed when the tread is running
def string_manipulation(connection_socket, client_address):
    while True:

        # receives a string from the client
        sentence = connection_socket.recv(1024).decode()

        # closes the connection socket if the client types quit
        if sentence == "quit":
            connection_socket.close()
            print("Client connection closed: ", client_address)
            break

        # changes the message received from the connection and sends it back
        capitalized_sentence = sentence.upper()
        print(capitalized_sentence)
        connection_socket.send(capitalized_sentence.encode())


# defines a new thread that uses the TCP connection socket to serve a client
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("New client connection: ", clientAddress)

    def run(self):
        string_manipulation(connectionSocket, clientAddress)


# creates a listening TCP socket
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")


while True:
    # accepts connections coming through the server socket
    connectionSocket, clientAddress = serverSocket.accept()

    # creates a new thread with the newly created connection socket
    t = MyThread()

    # starts the thread
    t.start()
