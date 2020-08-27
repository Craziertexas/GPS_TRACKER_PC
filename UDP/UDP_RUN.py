import socket
import UDP_SERVER

def UDP_RUN():
    UDP_SERVER.init_server("192.168.137.1",4000)
    i=0
    while True:
        print("#",i)
        UDP_SERVER.server_recive()
        i=i+1


if __name__ == '__main__':
    UDP_RUN()