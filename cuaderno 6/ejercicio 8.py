"""ejercicio 8"""

def Es_par(n):
    """int-->bool
    OBJ:Introduce un numero y dice si es par o no"""
    return n%2==0

def sumaRecursiva(fin):
    """int,int-->int
    OBJ:Introduce el numero hasta donde quiere que sume
        recursivamentey donde termina la suma"""
    suma=0
    for i in range(fin+1):
        if Es_par(i):
            suma+=i
        print("Si i toma como valor:,",i,",La suma de momento da:",suma)
    return suma

#Probadores
print("la suma da como resultado:",sumaRecursiva(50))
