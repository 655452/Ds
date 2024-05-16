import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5050

# List to hold all client connections
clients = []

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"[{client_address}] {message}")

            # Send a reply to the client
            reply = input("Enter your reply: ")
            client_socket.send(reply.encode('utf-8'))

            # Broadcast the received message to all other clients
            for c in clients:
                if c != client_socket:
                    c.send(f"[{client_address}] {message}".encode('utf-8'))
        except:
            # If there's an error, close the connection and remove the client
            print(f"[DISCONNECTED] {client_address} disconnected.")
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        
        # Add client socket to the list of clients
        clients.append(client_socket)
        
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
