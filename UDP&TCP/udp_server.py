import socket
import time

# Setting up the server
HOST = '127.0.0.1'  # host
PORT = 65433        # Port

def main():
    """sets up the UDP server and handles incoming packets"""
    
    # Creating a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind address and port
        server_socket.bind((HOST, PORT))
        print(f"[Start] UDP server is listening {HOST}:{PORT}")
        
        try:
            while True:
                # Receive data and client address
                data, addr = server_socket.recvfrom(1024)
                
                # Processing received data
                message = data.decode('utf-8')
                print(f"[Receive] Message from {addr}: {message}")
                
                # Constructing Response
                response = f"UDP server is already in {time.strftime('%Y-%m-%d %H:%M:%S')} receive your message: {message}"
                
                # Send Response
                server_socket.sendto(response.encode('utf-8'), addr)
                print(f"[Send] Replied to {addr}")
                
        except KeyboardInterrupt:
            print("\n[Close] UDP server closed")
        except Exception as e:
            print(f"[ERROR] Server error: {e}")

if __name__ == "__main__":
    main()
