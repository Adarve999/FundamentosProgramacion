
"ejercicio 8"

def validar_entero(n):
    try:
        int(n)
    except:
        resultado=False
    else:
        resultado=True
    
    return resultado

def rango_meses(n):
    return 1<= n <= 12

numero=input("Introduzca el numero, ")

if validar_entero(numero):
    numero=int(numero)
    if rango_meses(numero):
        if numero==1: print("Enero")
        elif numero==2: print("febrero")
        elif numero==3: print("marzo")
        elif numero==4: print("abril")
        elif numero==5: print("mayo")
        elif numero==6: print("junio")
        elif numero==7: print("julio")
        elif numero==8: print("agosto")
        elif numero==9: print("septiembre")
        elif numero==10: print("octubre")
        elif numero==11: print("noviembre")
        elif numero==12: print("diciembre")

    else:
        print("Es entero pero se sale del rango")
else:
    print("Lo introducido no es de tipo entero")