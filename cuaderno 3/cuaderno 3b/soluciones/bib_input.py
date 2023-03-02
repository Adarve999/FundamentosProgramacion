######################################
#  Biblioteca para validar entradas  #
######################################

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


def leer_real_rango(mensaje, min_value, max_value):
    """ str --> float
    OBJ: Solicita un número real al usuario entre los valores min y max.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = float(input(mensaje))
        except:
            print('Error: No es un número real.')
        else:
            if min_value <= numero <= max_value:
                es_valido = True
            else:
                print(f'Error: Fuera de rango [{min_value},{max_value}]')
    return numero
