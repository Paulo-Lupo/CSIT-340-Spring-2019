/*
 * Project 2 - UDP_Client.java
 * Joao Paulo D. S. Ferreira
 * CSIT 340 - Computer Networks
 * Dr. Dawei Li
 * March 25, 2019
 */

/* 
 * This program contains the client side of a UDP connection 
 * It sends a sentence to the server and receives it back in upper case.
 */

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UDP_Client {
	
	private final static int PORT = 5000;
	private final static String HOSTNAME = "localhost";
	
	public static void main(String[] args) {
		System.out.println("This is the UDP Client.");
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a sentence to convert to upper case. Type quit to quit: ");
		String requestString = scanner.nextLine();
		
		/* continue sending requests to the server until the user types quit */
		while(!requestString.toLowerCase().equalsIgnoreCase("quit")) {
			try {
				DatagramSocket socket = new DatagramSocket(0);
				

				/* sends the sentence to the server */
				byte[] requestBuffer = requestString.getBytes();
				InetAddress host = InetAddress.getByName(HOSTNAME);
				DatagramPacket request = new DatagramPacket(requestBuffer, requestBuffer.length, host, PORT);
				socket.send(request);
				
				/* receives the sentence back from the server */
				DatagramPacket response = new DatagramPacket(new byte[1024], 1024);
				socket.receive(response);
				String result = new String(response.getData());
				System.out.println(result);
				
				/* asks the user for another sentence */
				System.out.print("Enter a sentence to convert to upper case. Type quit to quit: ");
				requestString = scanner.nextLine();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		scanner.close();
	}
}
