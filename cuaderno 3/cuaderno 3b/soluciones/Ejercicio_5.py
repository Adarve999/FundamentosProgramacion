
def es_par(num):
    """int --> bool
    OBJ: Devuelve si un número es par
    """
    return num % 2 == 0

def dibujar_rectangulo(a,b):
    """ int,int -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones a por b utilizando la @ en las filas pares
        y la # en las impares
    """
    for i in range(a):
        for j in range(b):
            if es_par(i):
                print('@', end='')
            else:
                print('#', end='')
        print()


dibujar_rectangulo(5,5)
