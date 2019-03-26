/*
 * Project 2 - UDP_Server.java
 * Joao Paulo D. S. Ferreira
 * CSIT 340 - Computer Networks
 * Dr. Dawei Li
 * March 25, 2019
 */

/* 
 * This program contains the server side of a UDP connection 
 * It sends a receives a sentence from a client and sends it back in upper case.
 */

import java.io.*;
import java.net.*;

public class UDP_Server {
	
	private final static int PORT = 5000;
	private final static String HOSTNAME = "localhost";
	
	public static void main(String[] args) {
		
		System.out.println("This is the UDP Server.");
		try {
			DatagramSocket socket = new DatagramSocket(PORT);
			while(true) {
				
				/* receives the sentence from the client and converts it into a String. */
				DatagramPacket request = new DatagramPacket(new byte[1024], 1024);
				socket.receive(request);
				byte[] requestBuffer = request.getData();
				String requestString = new String(requestBuffer);
				
				/* sends back the sentence to the client in upper case */
				String responseString = requestString.toUpperCase();
				byte[] responseBuffer = responseString.getBytes();
				DatagramPacket response = new DatagramPacket(responseBuffer, responseBuffer.length, 
															 request.getAddress(), request.getPort());
				socket.send(response);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
