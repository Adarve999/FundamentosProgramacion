
"ejercicio 10"

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


CAMBIO = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

dinero = leer_real('Introduce la cantidad en €: ')
for moneda in CAMBIO:
    num_monedas = int(dinero // moneda)
    dinero = round(dinero % moneda, 2)
    if num_monedas > 0:
        if moneda < 5:
            print(f'Monedas de {moneda} euros: {num_monedas}')
        else:
            print(f'Billetes de {moneda} euros: {num_monedas}')
