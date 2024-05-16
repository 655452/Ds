import socket

def send_request(number, client_socket):
    client_socket.send(number.encode())
    response = client_socket.recv(1024)
    print("Factorial:", response.decode())

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    while True:
        number = input("Enter an integer to calculate factorial (or type 'exit' to quit): ")
        if number.lower() == 'exit':
            break

        try:
            # Attempt to convert the input to an integer
            n = int(number)
            # Send the integer value to the server
            send_request(str(n), client_socket)
        except ValueError:
            print("Invalid input. Please provide an integer or type 'exit' to quit.")

    client_socket.close()

if __name__ == "__main__":
    main()
