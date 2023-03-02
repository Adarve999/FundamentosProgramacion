
"ejercicio 9"

from math import sqrt

def validar_entero(n):
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    
    return resultado

a=input("introduce el valor de A:   ")

if validar_entero(a):
    a=float(a)
    b=input("introduce el valor de B:   ")

    if validar_entero(b):
        b=float(b)
        c=input("introduce el valor de C:   ")

        if validar_entero(c):
            c=float(c)

            discriminante=((b**2)-(4*a*c))
            
            if discriminante==0:
                operacion=(-b)/2*a
                print("el discriminante da 0 en este caso")
                print("da como resultado:",operacion)

            elif discriminante<0:
                print("RAICES IMAGINARIAS")
                print("en este caso el discriminante da negativo", discriminante)

            else:
                operacion=((-b+(sqrt(discriminante)))/2*a)
                print("la operacion da como resultado,   ",operacion)
        else:
            print("el valor de C no es de tipo float ")
    else:
        print("el valor de B no es de tipo float")
else:
    print("el valor de A no es de tipo float")        