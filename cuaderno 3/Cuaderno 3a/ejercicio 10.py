
"ejercicio 10"

def año_entero(n):
    try:
        int(n)
    except:
        resultado=False
    else:
        resultado=True

    return resultado

def es_bisiesto(n):
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)

año=input("Introduzca el año:   ")

if año_entero(año):
    año=int(año)
    if es_bisiesto(año):
	    print("Es bisiesto")
    else:
	    print("No es bisiesto")
else:
    print("Lo que has introducido no es de tipo INT")