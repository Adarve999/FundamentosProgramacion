
"ejercicio 15"

def es_float(n):
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado

def monomio(x,y):
    """float,float-->monomio
        OBJ:Introducir el coeficiente y el exponente
            y sacar el monomio por pantalla"""
    if es_float(x) and  es_float(y):
        x=float(x)
        y=float(y)
        if x == 0:
            print("no hay monomio resultante por ser un 0")
        elif x ==1:
            print("el monomio resultante es 1")
        elif y == 1:
            print("el monomio resultante es:    ",x)
        elif y == 0:
            print("No Se pone nada porque el exponente es 0")
        elif y < 0:
            print("El monomio es:   ","1/(",x,"x**",abs(y),")")
        else:
            print("El monomio es:   ",x,"x**",y)
    else:
        print("algunos de las variables introducidas no son de tipo FLOAT")

coeficiente=input("Introduzca el coeficiente:   ")
exponente=input("introduzca el exponente:   ")

monomio(coeficiente,exponente)