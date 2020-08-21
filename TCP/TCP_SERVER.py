import socket
from GUI import GUI

def init_server(server_ip,server_port):
    global server
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET=IPv4 // socket.SOCK_STREAM=TCP #CAMBIAR POR UDP
    server_address=(server_ip,server_port)
    server.bind(server_address) #Relate the protocol to the port Ip and Port
    print("Hello!! Im on {} at port {} :3".format(*server_address))

def connection_server():
    global server,i,connection
    i=0
    server.listen(1) #Listen for incoming conections
    sw_listen=True
    while sw_listen:
        i=0
        print("Waiting for connection :O")
        connection,clien_address=server.accept() #Get client Info #AGREGAR FILTRO IP
        #INPUT SWonnection_server(data_shared)
        try:
            data_raw = connection.recv(1024)  # Recieve message ##=Fixed Buffer
            sw_listen=False
            print("Conection from {} :D ".format(*clien_address))
        except:
            sw_listen=True
            print("Conection Failed :(")


def recieve_server():
    global i,connection
    socket.timeout(2)
    try:
        data_raw=connection.recv(1024)
        data=data_raw
        print('Package #',i,':',data.decode())
        i=i+1
        return data
    except TimeoutError:
        print("Timeout - No data recieved :/")
        connection_server()



def close_server():
    connection.close() #Close connection




