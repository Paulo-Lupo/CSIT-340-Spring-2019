# Project 5 - TCPMathServerPersistentMultithread.py
# Student Name: Joao Paulo D. S. Ferreira
# CSIT 340-01 - Computer Networks
# Dr. Dawei Li
# April 17, 2019

# This program implements a persistent TCP connection server.
# It uses multithreading to allow clients to use the server simultaneously.
# It evaluates math expressions requests from clients.

from socket import *
import threading


# defines the task to be executed when the tread is running
def evaluate_expression(connection_socket, client_address):
    while True:

        # receives an expression from the client as a string
        expression = connection_socket.recv(1024).decode()

        # closes the connection and finishes the thread if the user types quit
        if expression == "quit":
            connection_socket.close()
            print("Client connection closed: ", client_address)
            break

        # evaluates the input expression
        try:
            solution = str(eval(expression))

        except (SyntaxError, NameError):
            solution = "Invalid Input. Enter a valid input or type quit to quit"

        print(solution)

        # sends back the solution or error message
        connection_socket.send(solution.encode())


# defines a thread that uses the TCP connection socket to serve a client
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("New client connection: ", clientAddress)

    def run(self):
        evaluate_expression(connectionSocket, clientAddress)


# creates a listening TCP socket
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")


while True:

    # accepts connections coming through the server socket
    connectionSocket, clientAddress = serverSocket.accept()

    # creates a new thread with the newly created TCP connection socket
    t = MyThread()

    # starts the thread
    t.start()
