
#ejercicio 3

def Es_par(n):
    """int-->bool
    OBJ: Introducir un numero y averiguar si es par"""
    resultado=False
    if n%2==0:
        resultado=True
    return resultado

def ListaEnteros(lista):
    """lista,bool-->lista
    OBJ: Introducir una lista de tamaño X y meterla en una lista
        auxiliar de pares o impares"""
    pares=[]
    impares=[]
    for i in range(len(lista)):
        if Es_par(lista[i]):
            pares.append(lista[i])
        else:
            impares.append(lista[i])

    pares.sort()
    impares.sort(reverse=True)
    return pares,impares

#Probadores
print(ListaEnteros([2,4,5,1,2,4,6,7,5,0]))