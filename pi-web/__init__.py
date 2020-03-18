import socket

from .request import Request
from .responce import Responce



class Server:



    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.pages = {}

    def _log_event(log_message):
        print(log_message)


    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen()

        while 1:
            conn, addr = self.sock.accept()

            self._log_event("INFO Connected to: ", addr)

            byte_request = conn.recv(1024)

            if not byte_request:
                self._log_event("WARNING Request not recieved!")
                continue

            self._log_event("INFO Request Recieved! Contents:\n" + str(byte_request))

            resp = Responce(Request(byte_request))

            conn.send(resp.generate_responce(self.pages).encode())           # Sends back the responce generated in bytes.



    def stop_server(self):
        self.sock.close()



    def add_page(self, page_url, html):
        self.pages[page_url] = html


