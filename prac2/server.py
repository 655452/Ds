import socket
import concurrent.futures
import math

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Break the loop if no data received

            try:
                n = int(data.decode())
                result = calculate_factorial(n)
                client_socket.send(str(result).encode())
            except ValueError:
                client_socket.send("Invalid input. Please provide an integer.".encode())
    finally:
        client_socket.close()

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)  # Number of simultaneous connections the server can handle

print("Server listening on port 8080...")

# Use ThreadPoolExecutor to manage threads efficiently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection established with", client_address)
        
        # Submit the client handling task to the ThreadPoolExecutor
        executor.submit(handle_client, client_socket)
