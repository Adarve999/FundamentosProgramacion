
"ejercicio 12"

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

lista=[]

poblacion=leer_entero("¿Cuantos elementos tiene la varianza? ")

while len(lista)!=poblacion:
    gente=leer_entero("Introduzca el numero de poblacion-->")
    lista.append(gente)


m = sum(lista) / len(lista)
print("Este es el valor de la media: ", m)

var_res = sum((xi - m) ** 2 for xi in lista) / len(lista)
print("El valor de la varianza es el siguiente: ",var_res)