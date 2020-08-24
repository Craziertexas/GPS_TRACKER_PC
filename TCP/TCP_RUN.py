import TCP_CLIENT,TCP_SERVER

def TCP_RUN():
    try:
        selector=int(input("1: Receptor mode" + "\n" + "2: Transreceptor mode" + "\n"))
        if selector==1:
            server_address=input("Enter the server address: ")
            server_port=int(input("Enter the server port: "))
        else:
            server_address=input("Enter the server address: ")
            server_port=int(input("Enter the server port: "))
            client_address=input("Enter the client address: ")
            client_port=int(input("Enter the client port: "))
    except:
        sw=bool(input("\n"+"Input Error, wanna try again?" + "\n" + "True: input something" + "\n" + "False: Just press enter" + "\n"))
        
        if sw==True:
            TCP_RUN()
        else:
            exit()

    if selector==1:
        TCP_SERVER.init_server(server_address,server_port)
        TCP_SERVER.connection_server()
        while True:
            TCP_SERVER.recieve_server()

    if selector==2:
        TCP_SERVER.init_server(server_address, server_port)
        TCP_SERVER.connection_server()
        TCP_CLIENT.init_client(client_address, client_port)
        while True:
            TCP_CLIENT.sending_client(TCP_SERVER.recieve_server())
    

if __name__=="__main__":
    TCP_RUN()
