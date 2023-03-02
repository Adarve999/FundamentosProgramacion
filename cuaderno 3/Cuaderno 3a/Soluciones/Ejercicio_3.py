"""
Cuaderno de trabajo 3a.pdf - Ejercicio 3:
"""

def validar_entero(cadena):
    """ str --> bool
    OBJ: Comprueba que la cadena se puede convertir a entero
    """
    es_entero = False
    try:
        int(cadena)
        es_entero = True
    except:
        pass
    return es_entero

# Programa principal
a = input('Introduce un número: ')
if validar_entero(a):
    print('Es un número.')
    x = int(a)
else:
    print('No es un número.')