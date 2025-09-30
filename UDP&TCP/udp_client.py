import socket
import sys

# Set server
HOST = '127.0.0.1'  # host
PORT = 65433        # port

def main():
    """sends data to the UDP server and receives a response"""
    
    try:
        # Creating a UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            # Setting the timeout
            client_socket.settimeout(5)  # 5 seconds timeout
            
            # Getting User Input
            message = input("Please enter the message you want to send: ")
            
            # Send Message
            print(f"[Send] Sending message to {HOST}:{PORT}...")
            client_socket.sendto(message.encode('utf-8'), (HOST, PORT))
            
            # Receiving Response
            try:
                print("[Wait] Waiting for server response...")
                response, server_addr = client_socket.recvfrom(1024)
                
                # Print Response
                print(f"[Received] Response from {server_addr}: {response.decode('utf-8')}")
            except socket.timeout:
                print("[Timeout] Timed out waiting for server response.")
            
            print("[Complete] Communication completed")
            
    except KeyboardInterrupt:
        print("\n[Interrupt] User interrupt")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    main()
