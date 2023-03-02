

import bib_input

n = bib_input.leer_entero('Introduce un entero positivo: ')
if n > 0:
    for potencia in [2,3,5]:
        for exponente in range(n):
            print(f'{potencia**exponente:10}', end='')
        print()



