This project includes four Python programs that use TCP and UDP protocols for client-server communication.

Program Description
tcp_server.py: A TCP server that accepts multiple client connections and handles them using multithreading.

tcp_client.py: A TCP client that connects to the TCP server and sends/receives messages.

udp_server.py: A UDP server that processes incoming UDP packets.

udp_client.py: A UDP client that sends packets to the UDP server and receives responses.

How to Run code

TCP Communication
Start the TCP server first:

python tcp_server.py
Then, start the TCP client in another terminal:

python tcp_client.py
Enter a message in the client prompt and press send.

You can open multiple terminals and run multiple client instances to test multi-client functionality.

UDP Communication
Start the UDP server first:

python udp_server.py
Then, start the UDP client in another terminal:

python udp_client.py
Enter a message in the client prompt and press send.

Features
All programs include basic exception handling.

The client programs provide user interaction functionality.

The server logs timestamps for all received messages.
