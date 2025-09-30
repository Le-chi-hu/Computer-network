import socket
import sys

# Setting up the server
HOST = '127.0.0.1'  # Host
PORT = 65432        # Port

def main():
    """Main function, connects to the server and sends/receives messages"""
    
    try:
        # Creating a socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the server
            print(f"[Connect] Connecting to {HOST}:{PORT}...")
            try:
                client_socket.connect((HOST, PORT))
            except socket.error as e:
                print(f"[ERROR] Unable to connect to server: {e}")
                return
            
            print("[Connection successful] A connection has been established with the server")
            
            # Getting User Input
            message = input("Please enter the message to send: ")
            
            # Send Message
            print("[Send] Sending message...")
            client_socket.sendall(message.encode('utf-8'))
            
            # Receiving Response
            print("[Waiting] Waiting for server response...")
            response = client_socket.recv(1024)
            
            # Print Response
            print(f"[Receive] Server response: {response.decode('utf-8')}")
            
            print("[Complete] Communication completed")
            
    except KeyboardInterrupt:
        print("\n[Interrupt] User interrupt")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    main()
