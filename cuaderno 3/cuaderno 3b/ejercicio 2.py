"ejercicio 2"

def leer_entero_rango(mensaje, min_value, max_value):
    """ str --> int
    OBJ: Solicita un número entero al usuario entre los valores min y max.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = int(input(mensaje))
        except:
            print('Error: No es un número entero.')
        else:
            if min_value <= numero <= max_value:
                es_valido = True
            else:
                print(f'Error: Fuera de rango [{min_value},{max_value}]')
    return numero

min = 1
max = 12
print(leer_entero_rango(f'mes entre {min} y {max}: ',min,max))