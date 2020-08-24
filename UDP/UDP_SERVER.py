import socket

def init_server(server_ip,server_port):
    global server,i
    try:
        server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address=(server_ip,server_port)
        server.bind(server_address)
        i=0
        print("Hello!! Im on {} at port {} :3".format(*server_address))
    except:
        print("An error occurred during the server initialization")
    
def server_recive():
    global server,i
    data, address=server.recvfrom(1024)
    print("\n"+"Message: ",(data.decode()))
    print("From: ",(address))
    