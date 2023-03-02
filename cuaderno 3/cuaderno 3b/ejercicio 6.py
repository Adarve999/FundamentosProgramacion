
"ejercicio 6"

def leer_real(mensaje):
    """ str --> float
    OBJ: Solicita un número real al usuario hasta que se introduce correctamente.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = float(input(mensaje))
        except:
            print('Error: No es un número real.')
        else:
            es_valido = True
    return numero

limite = leer_real('Introduce el límite: ')
if limite > 0:
    contador = 0
    suma_armonica = 0
    while suma_armonica < limite:
        termino = 1 / (contador+1)
        suma_armonica += termino
        contador +=1
    print('El número de terminos es:', contador)
else:
    print('El límite es menor que 0.')

