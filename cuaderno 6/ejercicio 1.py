
"ejercicio 1"

def Esta_enLista(lista,numero):
    """lista,int-->bool
    OBJ:Introduce una lista y devuelve si esta o no en la lista"""
    i=0
    resultado=False
    while not resultado and i<len(lista):
        if lista[i]==numero:
            resultado=True
        i+=1
    return resultado
        

#Probadores
print(Esta_enLista([1,3,4,5,6,3,2,4,5],5))

print(Esta_enLista([1,3,4,5,6,3,2,4,5],0))
