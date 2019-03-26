/*
 * Project 2 - TCP_Client.java
 * Joao Paulo D. S. Ferreira
 * CSIT 340 - Computer Networks
 * Dr. Dawei Li
 * March 25, 2019
 */

/* 
 * This program contains the client side of a TCP connection 
 * It sends a sentence to the server and receives it back in upper case.
 */

import java.net.*;
import java.io.*;
import java.util.*;

public class TCP_Client {
	
	private static final int PORT = 5000;
	private static final String HOSTNAME = "localhost";

	public static void main(String[] args) {
		
		/* creates a Scanner object and asks the user for the first input */
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a sentence to convert to upper case. Type quit to quit: ");
		String line = scanner.nextLine();
		
		try {
			Socket socket = null;
			
			/* continues sending requests to the server until the user types quit */
			while (!line.toLowerCase().equalsIgnoreCase("quit")) {
				try {
					socket = new Socket(HOSTNAME, PORT);	
				} catch(UnknownHostException e) {
					e.printStackTrace();
				}
				
				DataOutputStream out = new DataOutputStream(socket.getOutputStream());
				DataInputStream in = new DataInputStream(socket.getInputStream());
				
				/* sends the sentence to the server and receives it back in upper case. */
				out.writeUTF(line);
				out.flush();
				String response = in.readUTF();
				System.out.println(response);
				out.close();
				in.close();
				socket.close();
				
				/* asks the user for another sentence */
				System.out.print("Enter a sentence to convert to upper case. Type quit to quit: ");
				line = scanner.nextLine();
			}
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
}