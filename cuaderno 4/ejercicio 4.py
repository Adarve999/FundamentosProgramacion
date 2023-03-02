
#ejercicio 4

def Es_mayor(n1,n2):
    """int,int-->bool
    OBJ:evalua dos valores y averigua cual es el mayor"""
    return n1>=n2

def Es_menor(n1,n2):
    """int,int-->bool
    OBJ:evalua dos valores y averigua cual es el mayor"""
    return n1<n2

def media(lista):
    """lista-->int
    OBJ:Introduce una lista con valores random y saca la media"""
    suma=0
    media=0
    menor=lista[0]
    mayor=lista[0]
    for i in range(len(lista)):
        suma+=lista[i]
        media=round(suma/len(lista),3)

        if Es_mayor(lista[i],mayor):
            mayor=lista[i]

        elif Es_menor(lista[i],menor):
            menor=lista[i]

    print("la media es: ",media)
    print("El numero mas grande es: ",mayor)
    print("El numero mas pequeño es: ",menor)

#probadores
media([1,2,4,5,3,5,6,0,3,4,5,1,24,5,99])