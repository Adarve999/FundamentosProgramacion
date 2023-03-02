"ejercicio 6"

def validar_entero(n):
    try:
        int(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado

n1=input("introduzca el 1º numero:")

if validar_entero(n1):
    n1=int(n1)
    n2=input("introduzca el 2º numero:")
    if validar_entero(n2):
        n2=int(n2)
        n3=input("introduzca el 3º numero:")
        if validar_entero(n3):
            n3=int(n3)
        else:
            print ("el 3º numero no es de tipo entero")
    else:
        print("el 2º numero no es de tipo entero")
else:
    print("el 1º numero no es de tipo entero")