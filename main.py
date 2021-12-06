import threading
from  threading import Thread,Semaphore
import time
import estacionamiiento 
esta=estacionamiiento
matriz=[['vacio','vacio','vacio'],['vacio','vacio','vacio'],['vacio','vacio','vacio']]


def entrada2():
    time.sleep(0.60)
    esta.entrada(matriz)

def salida2():
    time.sleep(0.60)
    esta.salida(matriz)
    

for  n in range(30):

    dato=esta.ispecion(matriz)
    if dato=='lleno':
        print('estacionamiento lleno')
        hilo2=threading.Thread(target=salida2)
        hilo2.start()
        hilo2.join()

    else:

        hilo1 = threading.Thread(target=entrada2)
        hilo1.start()
        hilo1.join()
        hilo2=threading.Thread(target=salida2)
        hilo2.start()
        hilo2.join()
        


