
"ejercicio 5"

def inversion(lista):
    """list-->cadena
    OBJ:Obtener la cadena en una lista y darla la vuelta"""
    palabraInvertida=""
    for i in range(len(lista)-1,-1,-1):
        palabraInvertida+=lista[i]
    return palabraInvertida
    
#Probadores
palabra="Hola como estas"
print(palabra)
print(inversion(palabra))
