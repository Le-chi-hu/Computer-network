import socket
import threading
import time

# Setting up the server
HOST = '127.0.0.1'  # Host
PORT = 65432        # Ports
MAX_CONNECTIONS = 5  # Maximum number of connections

def handle_client(conn, addr):
    """
Functions that handle a single client connection
 conn: client connection socket
 addr: client address
    """
    print(f"[New Connection] {addr} connected.")
    
    try:
        # Receiving client messages
        data = conn.recv(1024)
        if not data:
            print(f"[{addr}] No data received")
            return
            
        # Output received messages
        message = data.decode('utf-8')
        print(f"[{addr}] Receive message: {message}")
        
        # Process the message and respond
        response = f"The server is already in {time.strftime('%Y-%m-%d %H:%M:%S')} Received your message: {message}"
        
        # Send Response
        conn.sendall(response.encode('utf-8'))
        print(f"[{addr}] Responded")
        
    except Exception as e:
        print(f"[ERROR] {addr} Handling Errors: {e}")
    finally:
        # Close the connection
        conn.close()
        print(f"[Close] {addr} connection closed")

def main():
    """setting up the TCP server and accepting connections"""
    
    # Create a server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # avoid reuse
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind address and port
        server_socket.bind((HOST, PORT))
        
        # Start monitoring
        server_socket.listen(MAX_CONNECTIONS)
        print(f"[Start] Server is listening on {HOST}:{PORT}")
        
        try:
            while True:
                # Accept client connection
                conn, addr = server_socket.accept()
                
                # Create a thread for a new connection
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.daemon = True  # Set as a daemon thread, the thread will exit when the main program exits
                client_thread.start()
                # print(f"Current Threads: {threading.enumerate()}")
                print(f"[Active Connections] {threading.active_count() - 2}")
                
        except KeyboardInterrupt:
            print("\n[Close] Server shutdown")
        except Exception as e:
            print(f"[ERROR] Server error: {e}")

if __name__ == "__main__":
    main()
