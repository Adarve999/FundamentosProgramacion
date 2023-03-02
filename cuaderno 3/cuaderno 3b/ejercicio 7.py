
"ejercicio 7"

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

def tabla(n):
    for i in [2,3,5]:
        for j in range(1,n):
            print(i**j, end=" ")

        print()    

entero=leer_entero("introduce el numero:    ")
tabla(entero)