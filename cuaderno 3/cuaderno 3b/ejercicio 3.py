
"ejercicio 3"

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

cuantos = leer_entero('¿Cuántos números se van a introducir? ')

if cuantos <= 2:
    print('Tienes que poner más de dos números')
else:
    numero =leer_entero('Introduce un número: ')
    suma = numero
    mayor = numero
    menor = numero
    for i in range(1, cuantos):
        numero =leer_entero('Introduce un número: ')
        suma += numero
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    media = suma / cuantos
    print("El mayor es", mayor)
    print("El menor es", menor)
    print("El media es", media)
