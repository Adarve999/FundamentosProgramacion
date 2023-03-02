
"ejercicio 3"

def validar_entero(n):
    """?-->int
    OBJ: introduzca algo y que verifique cual es entero"""
    try:
        int (n)
    except:
        resultado=False
    else:
        resultado=True

    return resultado

Numero=input("Introduzca un numero o lo que quiera: ")

if validar_entero(Numero):
    print(" es un entero,",Numero)
else:
    print("ha introducido otra cosa que no es un entero, ",Numero,",  de tipo--> ",type(Numero))