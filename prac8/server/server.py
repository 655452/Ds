import os
from xmlrpc.server import SimpleXMLRPCServer

class FileTransferServer:
    def __init__(self, address):
        self.server = SimpleXMLRPCServer(address, allow_none=True)
        self.server.register_function(self.receive_file, 'receive_file')
        self.server.register_function(self.download_file, 'download_file')

    def receive_file(self, file_data, file_name):
        try:
            with open(file_name, 'wb') as f:
                f.write(file_data.data)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def download_file(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def serve_forever(self):
        print("File Transfer Server is running...")
        self.server.serve_forever()

if __name__ == "__main__":
    server_address = ('localhost', 8000)
    file_transfer_server = FileTransferServer(server_address)
    file_transfer_server.serve_forever()
