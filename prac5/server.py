import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received message from {client_address}: {message}")
        client_socket.send(f"Server received your message: {message}".encode())
    client_socket.close()

def server():
    host = 'localhost'
    port = 8080
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for incoming connections
    
    print(f"Server is listening on port {port}...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    server()
