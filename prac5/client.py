import socket
import threading

def send_message(client_socket):
    while True:
        message = input("Enter message to send to server (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        print("Server response:", response.decode())

def client():
    host = 'localhost'
    port = 8080
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print(f"Connected to server on port {port}")
    
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()
    send_thread.join()  # Wait for the send_thread to finish
    client_socket.close()

if __name__ == "__main__":
    client()
