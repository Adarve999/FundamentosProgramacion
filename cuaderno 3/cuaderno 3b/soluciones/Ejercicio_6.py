
import bib_input

limite = bib_input.leer_real('Introduce el límite: ')
if limite > 0:
    contador = 0
    suma_armonica = 0
    while suma_armonica < limite:
        termino = 1 / (contador+1)
        suma_armonica += termino
        contador +=1
    print(f'El número de terminos es: {contador}')
else:
    print('El límite es menor que 0.')
