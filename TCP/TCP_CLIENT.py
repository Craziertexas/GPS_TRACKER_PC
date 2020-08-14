import socket
import time


def init_client(toserver_ip,toserver_port):
    global client
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET=IPv4 // socket.SOCK_STREAM=TCP
    client_address=(toserver_ip,toserver_port)
    try:
        client.connect(client_address) #Conect the client to the server
        print("Hello!! Im going to {} at port {} :3".format(*client_address))
    except:
        print("Connection Failed :(")

def sending_client(data):
    global client
    if data:
        try:
            print("Seeeeeeending... ")
            client.sendall(data)
            print("Done :P")
        except:
            print("Sending Failed")
            print("Retrying on 10 seconds...")
            time.sleep(10)
            init_client()
    else:
        print("No Data")
        print("Retrying on 1 second ")
        time.sleep(1)
        sending_client(data)


