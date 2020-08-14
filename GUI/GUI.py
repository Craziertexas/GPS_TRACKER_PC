import tkinter as tk
from tkinter import Tk,ttk



def init_gui():
    global Variable_Server_Ip,Variable_Client_Ip,Variable_Server_Port,Variable_Client_Port,Variable_Sw_Server
    #Basic setup
    window=Tk()
    window.geometry("800x400")
    window.configure(bg="white")
    window.title("GPS TCP TRANSRECEPTOR")
    window.resizable(height=False,width=False)
    #Variables
    Variable_Server_Ip=tk.StringVar(value="192.168.137.1")
    Variable_Client_Ip=tk.StringVar(value="192.168.137.103")
    Variable_Server_Port=tk.StringVar(value="4000")
    Variable_Client_Port=tk.StringVar(value="5000")
    Variable_Sw_Server=tk.IntVar(value=True)
    #Labels
    Label_Server_Ip=ttk.Label(window,text="SERVER IP:").place(x=50,y=50)
    Label_Client_Ip=ttk.Label(window,text="CLIENT IP:").place(x=250,y=50)
    Label_Server_Port=ttk.Label(window,text="SERVER PORT:").place(x=30,y=80)
    Label_Client_Port=ttk.Label(window,text="CLIENT PORT:").place(x=235, y=80)
    Label_Protocol_Mode = ttk.Label(window, text="PROTOCOL:").place(x=450,y=50)
    #Buttons
    Button_Start_Server=ttk.Button(window,text="START SERVER",command=quit).place(x=110,y=110)
    Button_Connect_Client=ttk.Button(window,text="CONNECT CLIENT",command=quit).place(x=320,y=110)
    Button_Transmit_Client=ttk.Button(window,text="TRANSMIT",command=EXEC.quit).place(x=320,y=140)
    Button_Stop_Client=ttk.Button(window,text="STOP TRASMISSION",command=quit).place(x=320,y=170)
    Button_Restart=ttk.Button(window,text="RESTART",command=quit).place(x=650,y=350)
    Button_Exit=ttk.Button(window,text="EXIT",command=quit).place(x=700,y=350)
    #Entrys
    Entry_Server_Ip=ttk.Entry(window, textvariable=Variable_Server_Ip).place(x=110,y=50)
    Entry_Client_Ip = ttk.Entry(window, textvariable=Variable_Client_Ip).place(x=310, y=50)
    Entry_Server_Port = ttk.Entry(window, textvariable=Variable_Server_Port).place(x=110,y=80)
    Entry_Client_Port = ttk.Entry(window, textvariable=Variable_Client_Port).place(x=310,y=80)
    #CheckButton
    CheckButton_Sw_Server = ttk.Checkbutton(window,text="RECIEVE DATA",variable=Variable_Sw_Server,onvalue=1,offvalue=0).place(x=110,y=170)

    window.mainloop()

def IP_SERVER_VARIABLES():
    Server_Ip=Variable_Server_Ip.get()
    Server_Port=int(Variable_Server_Port.get())
    return Server_Ip,Server_Port

def IP_CLIENT_VARIABLES():
    Client_Ip=Variable_Client_Ip.get()
    Client_Port=int(Variable_Client_Port.get())
    return Client_Ip,Client_Port

def DISABLE_SERVER_VARIABLES():
    global Variable_Sw_Server
    Sw_Server=bool(Variable_Sw_Server.get())
    return Sw_Server

def Transreceptor():
    print("Transreceptor")

