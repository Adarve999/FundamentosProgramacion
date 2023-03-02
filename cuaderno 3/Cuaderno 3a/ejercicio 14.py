
"ejercicio 14"

def es_float(n):
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado


def baremo(n):
    """float-->int
        OBJ: Introducir ingresos familiares y obtener la puntuacion
             en funcion de los ingresos"""
    puntos=-1
    if es_float(n):
        n=float(n)

        if 0 <= n < 1800: 
            puntos=4
        elif 1800 <= n < 3500: 
            puntos=3
        elif 3500 <= n < 5000: 
            puntos=2
        elif n >= 5000: 
            puntos=1

    return puntos

ingreso=input("Introduzca los ingresos de su unidad familiar(€):    ")

print("Por sus ingresos familiares sus puntos son-->",baremo(ingreso))