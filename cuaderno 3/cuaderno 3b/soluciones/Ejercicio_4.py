
import bib_input

total = 0
positivos = 0
negativos = 0
numero = bib_input.leer_entero('Introduce un número: ')
while numero != -9999:
    total += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    numero = bib_input.leer_entero('Introduce un número: ')


print(f'Has introducido {total} números.')
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
