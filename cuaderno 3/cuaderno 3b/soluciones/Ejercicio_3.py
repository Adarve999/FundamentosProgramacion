
import bib_input

cuantos = bib_input.leer_entero('¿Cuántos números se van a introducir? ')
if cuantos <= 2:
    print('Tienes que poner más de dos números')
else:
    numero = bib_input.leer_entero('Introduce un número: ')
    suma = numero
    mayor = numero
    menor = numero
    for i in range(1, cuantos):
        numero = bib_input.leer_entero('Introduce un número: ')
        suma += numero
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    media = suma / cuantos
    print(f'El mayor es {mayor}')
    print(f'El menor es {menor}')
    print(f'La media es {media}')
