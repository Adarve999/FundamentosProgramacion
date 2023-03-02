
"ejercicio 13"

def leer_real(mensaje):
    """ str --> float
    OBJ: Solicita un número real al usuario hasta que se introduce correctamente.
    """
    es_valido = False
    while not es_valido:
        try:
            numero = input(mensaje)
        except:
            print('Error: Se ha introducido algo erroneo.')
        else:
            es_valido = True
    return numero


simbolo=leer_real("Introduzca el caracter a ver si adivina: ")
intento=0

while simbolo != '#' and intento!=10:
    simbolo = leer_real('Ese no es el símbolo oculto. Haga su apuesta: ')
    intento += 1

if simbolo!="#":
    print("Lo siento se te han acabado los",intento,"intentos, y no has conseguido lograrlo")
else:
    print(f'Por fin! Ha necesitado {intento} intentos para adivinarlo.')