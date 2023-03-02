
"ejercicio 1"

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

entero=leer_entero("introduzca un numero entero:   ")