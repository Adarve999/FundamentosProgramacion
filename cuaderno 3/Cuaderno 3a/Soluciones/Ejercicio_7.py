"""
Cuaderno de trabajo 3a.pdf - Ejercicio 7:
"""

def es_vocal(caracter):
    """ str --> bool
    OBJ: Indica si un caracter es una vocal o no (incluye mayúsculas)
    """
    if caracter == 'a' or caracter == 'A':
        salida = True
    elif caracter == 'e' or caracter == 'E':
        salida = True
    elif caracter == 'i' or caracter == 'I':
        salida = True
    elif caracter == 'o' or caracter == 'O':
        salida = True
    elif caracter == 'u' or caracter == 'U':
        salida = True
    else:
        salida = False
    return salida

def es_vocal_or(caracter):
    """ str --> bool
    OBJ: Indica si un caracter es una vocal o no (incluye mayúsculas)
    """
    return caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or \
        caracter == 'i' or caracter == 'I' or caracter == 'o' or caracter == 'O' or \
        caracter == 'u' or caracter == 'U'


# Programa principal
cadena = input('Introduce un caracter: ')
print(f'Es vocal (if-else): {es_vocal(cadena)}')
print(f'Es vocal (or): {es_vocal_or(cadena)}')
