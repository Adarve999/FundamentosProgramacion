
"ejercicio 7"

def validar_string(n):
    try:
        str(n)
    except:
        resultado=False
    else:
        resultado=True
        
    return resultado

caracter=input("introduce un caracter:  ")

#FORMA CON OR
if validar_string(caracter):
    if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
        print("es una vocal este caracter, ", caracter)
    else:
        print("NO es una vocal este caracter, ",caracter)


#FORMA CON IF Y ELIF
if validar_string(caracter):
    if caracter=="a":
        print("es una vocal este caracter, ", caracter)
    elif caracter=="e":
        print("es una vocal este caracter, ", caracter)
    elif caracter=="i":
        print("es una vocal este caracter, ", caracter)
    elif caracter=="o":
        print("es una vocal este caracter, ", caracter)
    elif caracter=="u":
        print("es una vocal este caracter, ", caracter)
else:
    print("NO es una vocal este caracter, ",caracter)