
"ejercicio 14"

import numpy as np
import matplotlib.pyplot as plt

def leer_entero(mensaje):
    """ str --> int
    OBJ: Solicita un número entero al usuario hasta que se introduce correctamente.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = int(input(mensaje))
        except:
            print('Error: No es un número entero.')
        else:
            es_valido = True
    return numero

def leer_real(mensaje):
    """ str --> float
    OBJ: Solicita un número real al usuario hasta que se introduce correctamente.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = float(input(mensaje))
        except:
            print('Error: No es un número real.')
        else:
            es_valido = True
    return numero

n=leer_entero("¿cuantos numeros van a introducirse? ")
s=leer_real("cual va a ser el incremento")

x=np.zeros([n])
y1=np.zeros([n])
y2=np.zeros([n])

#SUMATORIOS
sy1=np.zeros([n])
sy2=np.zeros([n])

for i in range(1,n):
    x[i]=x[i-1]+s
    y1[i]=1/x[i]
    y2[i]=1/pow(x[i],2)
    sy1[i]=sy1[i-1]+y1[i]
    sy1[i]=sy2[i-1]+y2[i]



