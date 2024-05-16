import socket
import threading

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except OSError:
            break

def send_messages(client_socket):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Start a new thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Start a new thread to send messages to the server
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    start_client()
