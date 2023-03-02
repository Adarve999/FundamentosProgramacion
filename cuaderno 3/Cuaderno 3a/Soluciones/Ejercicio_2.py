"""
Cuaderno de trabajo 3a.pdf - Ejercicio 2:
"""

def convertir_hora(hora, minutos):
    """ int, int --> str
    OBJ: Convierte una hora en formato 24h a 12h
    """
    resultado = ''
    if 0 <= hora <= 23 and 0 <= minutos <= 59:
        if hora == 0:
            resultado = f'12:{minutos} AM'
        elif hora > 12:
            resultado = f'{hora-12}:{minutos} PM'
        else:
            resultado = f'{hora}:{minutos} AM'
    return resultado


# Programa principal
try:
    hora = int(input('Introduce la hora: '))
    min = int(input('Introduce los minutos: '))
except:
    print('El valor introducido no es entero')
else:
    hora12 = convertir_hora(hora,min)
    if hora12 == '':
        print('La hora no es válida')
    else:
        print(f'La hora en formato 12h es {hora12}')