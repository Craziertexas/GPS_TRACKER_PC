from GUI import GUI
from TCP import TCP_RUN
from threading import Thread
import queue
#COMPARTIR VARIABLES ENTRE THREADS

def TEST(share):
    while True:
        print(share.get())

if __name__=="__main__":
    share=queue.Queue()
    share.put("Default")
    Process1=Thread(target=TCP_RUN,args=(share,))
    Process2=Thread(target=TEST,args=(share,))
    Process1.start()
    Process2.start()
    Process1.join()
    Process2.join()



