"""
Cuaderno de trabajo 3a.pdf - Ejercicio 12:
"""

import math

opcion = -1
while opcion != 0:
    print('\t1. Seno')
    print('\t2. coseno')
    print('\t3. Tangente')
    print('\t4. Cotangente')
    print('\t5. Secante')
    print('\t6. Cosecante')
    print('\t0. Salir')
    try:
        opcion = int(input('Elija una opción: '))
    except:
        print('La opción no es válida')
    else:
        if 1 <= opcion <= 6:
            try:
                angulo = float(input('Introduzca un angulo (en radianes): '))
            except:
                print('El ángulo introducido no es válido')
            else:
                if opcion == 1:
                    print(f'El seno es {math.sin(angulo)}')
                elif opcion == 2:
                    print(f'El coseno es {math.cos(angulo)}')
                elif opcion == 3:
                    print(f'La tangente es {math.tan(angulo)}')
                elif opcion == 4:
                    print(f'La cotangente es {math.atan(angulo)}')
                elif opcion == 5:
                    print(f'La secante es {1 / math.cos(angulo)}')
                elif opcion == 6:
                    print(f'La cosecante es {1 / math.sin(angulo)}')
