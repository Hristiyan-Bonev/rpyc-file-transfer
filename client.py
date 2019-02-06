from socket import gaierror
import socket
import sys
import rpyc

class FileCopyInterface:
    '''
    Interface to share files between host and server
    '''
    def __init__(self, file, ip_address='192.168.0.102', port=18812):
        self.ip_address = ip_address
        self.port = port
        self._connect()
        if not file:
            # If file is not provided
            print("Please provide a file!")
        else:
            self._transfer_data(file)

    def _connect(self):
        try:
            # Initialize connection with provided parameters
            self.conn = rpyc.connect(self.ip_address, self.port)
        except gaierror:
            # Catch if target is not reachable.
            print("Target unreachable. Check provided IP adress and port")

    def _transfer_data(self, file):
        # Open file in binary mode
        with open(file, 'rb') as f:
            self.conn.root.get_data(file, f)

if __name__ == '__main__':
    # Using default IP and port: 192.168.102 and port 18812
    file = sys.argv[1] if len(sys.argv) > 1 else None
    file_copier = FileCopyInterface(file)
