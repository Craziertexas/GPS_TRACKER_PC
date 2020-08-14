import tkinter as tk
from tkinter import Tk,ttk
from TCP import TCP_SERVER
from TCP import TCP_CLIENT

class GUI():
    def __init__(self):
        #Basic setup
        window=Tk()
        window.geometry("800x400")
        window.configure(bg="white")
        window.title("GPS TCP TRANSRECEPTOR")
        window.resizable(height=False,width=False)
        #Variables
        self.Variable_Server_Ip=tk.StringVar(value="192.168.137.1")
        self.Variable_Client_Ip=tk.StringVar(value="192.168.137.173")
        self.Variable_Server_Port=tk.StringVar(value="4000")
        self.Variable_Client_Port=tk.StringVar(value="5000")
        #Labels
        Label_Server_Ip=ttk.Label(window,text="SERVER IP:").place(x=50,y=50)
        Label_Client_Ip=ttk.Label(window,text="CLIENT IP:").place(x=250,y=50)
        Label_Server_Port=ttk.Label(window,text="SERVER PORT:").place(x=30,y=80)
        Label_Client_Port=ttk.Label(window,text="CLIENT PORT:").place(x=235, y=80)
        Label_Protocol_Mode = ttk.Label(window, text="PROTOCOL:").place(x=450,y=50)
        #Buttons
        Button_Start_Server=ttk.Button(window,text="START SERVER",command=self.Start_Server).place(x=110,y=110)
        Button_Connections_Server=ttk.Button(window,text="ENABLE CONNECTIONS",command=TCP_SERVER.connection_server).place(x=110,y=140)
        Button_Disconnect_Server=ttk.Button(window,text="DISCONNECT",command=TCP_SERVER.close_server).place(x=110,y=170)
        Button_Connect_Client=ttk.Button(window,text="CONNECT CLIENT",command=self.Start_Client).place(x=320,y=110)
        Button_Transmit_Client=ttk.Button(window,text="TRANSMIT",command=self.Transreceptor).place(x=320,y=140)
        Button_Stop_Client=ttk.Button(window,text="STOP",command=quit).place(x=320,y=170)
        #Entrys
        Entry_Server_Ip=ttk.Entry(window, textvariable=self.Variable_Server_Ip).place(x=110,y=50)
        Entry_Client_Ip = ttk.Entry(window, textvariable=self.Variable_Client_Ip).place(x=310, y=50)
        Entry_Server_Port = ttk.Entry(window, textvariable=self.Variable_Server_Port).place(x=110,y=80)
        Entry_Client_Port = ttk.Entry(window, textvariable=self.Variable_Client_Port).place(x=310,y=80)

        window.mainloop()

    def Start_Server(self):
        Server_Ip=self.Variable_Server_Ip.get()
        Server_Port=int(self.Variable_Server_Port.get())
        TCP_SERVER.init_server(Server_Ip,Server_Port,)

    def Start_Client(self):
        Client_Ip=self.Variable_Client_Ip.get()
        Client_Port=int(self.Variable_Client_Port.get())
        TCP_CLIENT.init_client(Client_Ip,Client_Port)

    def Transreceptor(self):
        Sw_Transreceptor=True
        while Sw_Transreceptor:
            TCP_CLIENT.sending_client(TCP_SERVER.recieve_server())

if __name__=="__main__":
    GUI()
