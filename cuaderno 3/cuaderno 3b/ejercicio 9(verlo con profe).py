
"ejercicio 9"

def leer_entero_rango(mensaje, min_value, max_value):
    """ str --> int
    OBJ: Solicita un número entero al usuario entre los valores min y max.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = int(input(mensaje))
        except:
            print('Error: No es un número entero.')
        else:
            if min_value <= numero <= max_value:
                es_valido = True
            else:
                print(f'Error: Fuera de rango [{min_value},{max_value}]')
    return numero

año=leer_entero_rango("introduzca el año:   ",1,2000)

Letras=["M","D","C","L","X","V","I"]
años = [1000,500,100,50,10,5,1]

dinero = leer_entero_rango("introduzca el año:   ",1,2000)
for moneda in años:
    num_monedas = int(dinero // moneda)
    dinero = round(dinero % moneda, 2)
    if num_monedas > 0:
        print(f'Año de {moneda} : {num_monedas}')
