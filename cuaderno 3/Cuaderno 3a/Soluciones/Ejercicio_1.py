"""
Cuaderno de trabajo 3a.pdf - Ejercicio 1:
"""

try:
    importe = float(input('Introduce el importe de la compra: '))
except:
    print('ERROR: El importe no es un número')
else:
    if importe > 100:
        tarjeta = input('¿Ha pagado con tarjeta (si/no)? ')
        if tarjeta == 'si':
            print(f'Tiene que pagar {importe*0.98}')
        elif tarjeta == 'no':
            print(f'Tiene que pagar {importe*0.95}')
        else:
            print('La respuesta no es correcta')
    else:
        print(f'Tiene que pagar {importe}')