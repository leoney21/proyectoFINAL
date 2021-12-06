import random



def visualizar(matriz):
    
    for f in matriz:
        for c in f:
         print(c,end='|')
        print()   

def  entrada(matriz):

   print('entrada')
   matriz[random.randint(0,2)][random.randint(0,2)]='lleno'
   matriz[random.randint(0,2)][random.randint(0,2)]='lleno'
   visualizar(matriz)
   return matriz
    
               
def salida(matriz):
   print('salida')
   matriz[random.randint(0,2)][random.randint(0,2)]='vacio'
   visualizar(matriz)
   return matriz

def ispecion(matriz):
    for f in range(len(matriz)):
            for c in range(len(matriz[f])):
                espacio= matriz[f][c]
                if espacio =='vacio':
                    return 'vacio'
                else:

                      return 'lleno'




          


    
