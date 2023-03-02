
#Ejercicio 2

def Es_igual(lista1,lista2):
    """lista,lista->lista
    OBJ:averiguar si tienen el mismo tamaño y sumar las listas"""
    suma=[]
    if len(lista1)==len(lista2):
        for i in range(len(lista1)):
            suma.append(lista1[i]+lista2[i])

    elif len(lista1)<len(lista2):
        for i in range(len(lista1)):
            suma.append(lista1[i]+lista2[i])
        for r in range(len(lista1),len(lista2)):
            suma.append(lista2[r])
            
    elif len(lista1)>len(lista2):
        for i in range(len(lista2)):
            suma.append(lista1[i]+lista2[i])
        for r in range(len(lista2),len(lista1)):
            suma.append(lista1[r])        
    return suma

#Probadores

print(Es_igual([1,2,4],[1,5,6]))
print(Es_igual([1,2,4],[1,5,6,4]))
print(Es_igual([1,2,4,5,6],[1,5,6,4]))