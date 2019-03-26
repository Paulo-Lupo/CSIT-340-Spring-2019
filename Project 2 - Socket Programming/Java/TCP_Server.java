/*
 * Project 2 - TCP_Server.java
 * Joao Paulo D. S. Ferreira
 * CSIT 340 - Computer Networks
 * Dr. Dawei Li
 * March 25, 2019
 */

/* 
 * This program contains the server side of a TCP connection 
 * It sends a receives a sentence from a client and sends it back in upper case.
 */

import java.net.*;
import java.io.*;
public class TCP_Server {
	private static int PORT = 5000;
	public static void main(String[] args) {
		try {
			
			/* opens the server */
			ServerSocket server = new ServerSocket(PORT);
			System.out.println("This is the TCP Server");
			while(true) {
				
				Socket connectionSocket = server.accept();
				System.out.println("Client Accepted.");
				
				DataInputStream in = new DataInputStream(connectionSocket.getInputStream());
				DataOutputStream out = new DataOutputStream(connectionSocket.getOutputStream());
				
				/* reads in the sentence from the client and does the conversion */
				String line = in.readUTF();
				String newLine = line.toUpperCase();
				out.writeUTF(newLine);
				out.flush();
				
				/* closes the connection */
				System.out.println("Closing Connection.");
				connectionSocket.close();
				in.close();
				out.close();
			}
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
}
