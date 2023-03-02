
"ejercicio 4"

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

valor=leer_entero("Introduzca un numero -9999 para salir:   ")
positivo=0
negativos=0
while valor !=-9999:
    valor=leer_entero("Introduzca un numero -9999 para salir:   ")
    if valor>0:
        positivo+=1
    elif valor<0:
        negativos+=1

print("el numero de positivos es:   ",positivo)
print("el numero de negativos es :  ",negativos)
    