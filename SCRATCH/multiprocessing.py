from multiprocessing import process

def hola():
    print("Hola")

def multi():
    print("multi")

def adios():
    print("adios")

if __name__=="__main__":
    p1=process(target=hola)
    p2=process(target=multi)
    p1.start()
    p2.start()
    p1.join()
    p2.join()