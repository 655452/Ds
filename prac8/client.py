import xmlrpc.client
import os

class FileTransferClient:
    def __init__(self, server_address):
        self.server = xmlrpc.client.ServerProxy(f"http://{server_address[0]}:{server_address[1]}")

    def upload_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                file_data = xmlrpc.client.Binary(f.read())
                file_name = os.path.basename(file_path)
                return self.server.receive_file(file_data, file_name)
        except Exception as e:
            print(f"Error: {e}")
            return False

    def download_file(self, file_name):
        try:
            file_data = self.server.download_file(file_name)
            with open(file_name, 'wb') as f:
                f.write(file_data.data)
            print(f"{file_name} downloaded successfully.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    server_address = ('localhost', 8000)
    client = FileTransferClient(server_address)

    while True:
        print("\nMenu:")
        print("1. Upload a file")
        print("2. Download a file")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path of the file to upload: ")
            if client.upload_file(file_path):
                print("File uploaded successfully.")
        elif choice == '2':
            file_name = input("Enter the name of the file to download: ")
            client.download_file(file_name)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
