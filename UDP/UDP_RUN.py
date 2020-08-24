import socket
import UDP_SERVER

def UDP_RUN():
    UDP_SERVER.init_server("192.168.137.1",4000)
    while True:
        UDP_SERVER.server_recive()


if __name__ == '__main__':
    UDP_RUN()