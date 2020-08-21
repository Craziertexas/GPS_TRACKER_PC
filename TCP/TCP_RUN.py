from TCP import TCP_CLIENT,TCP_SERVER

def TCP_RUN():
    TCP_SERVER.init_server("192.168.137.1", 4000)
    TCP_SERVER.connection_server()
    TCP_CLIENT.init_client("192.168.137.173", 4000)
    while True:
        TCP_CLIENT.sending_client(TCP_SERVER.recieve_server())

if __name__=="__main__":
    TCP_RUN()
