import rpyc
from rpyc.utils.server import ThreadedServer


class FileTransferServer(rpyc.Service):
    '''
    Service for receiving files.
    '''
    def on_connect(self, conn):
	    print('Connection established')
    def on_disconnect(self, conn):
	    print('Connection destroyed')
    def exposed_get_data(self, filename, file):
	     print('Incoming file trasfer...')
             with open(filename, 'wb') as f:
		     for line in file:
			     f.write(line)
             print('Transfer finished!')


if __name__ == "__main__":
    t = ThreadedServer(FileTransferServer, port=18812)
    t.start()
