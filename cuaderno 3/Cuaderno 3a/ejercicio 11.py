
"ejercicio 11"

def es_entero(n):
    try:
        int(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado

def Ordenacion(x,y):
    return ord(x) > ord(y)

def es_par(n):
    return n % 2 == 0

def es_primo(n):
    esPrimo=True
    for i in range(2,n):
        if n % i ==0:
            esPrimo=False
            break
    return esPrimo

n1=input("Introduzca el primer caracter: ")
n2=input("Introduzca el segundo caracter: ")

if Ordenacion(n1,n2):
    print("el orden correcto segun su codigo ASCI de Mayor a menor es: ",n1 ,"y despues",n2)
    if es_entero(n1):
        n1=int(n1)
        if es_par(n1):
            print(n1," ,es par")    
        elif es_primo(n1):
            print(n1," ,es primo")
        else:
            print(n1," ,no es primo ni tampoco par")
    else:
        print(n1," , no es una cifra")
else:
    print("el orden correcto segun su codigo ASCI de Mayor a menor es: ",n2 ,"y despues",n1)
    if es_entero(n2):
        n2=int(n2)
        if es_par(n2):
            print(n2," ,es par")
        elif es_primo(n2):
            print(n2," ,es primo")
        else:
            print(n2," ,no es primo ni tampoco par")
    else:
        print(n2," , no es una cifra")
