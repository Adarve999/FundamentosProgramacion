
#ejercicio 10

def Vocales(vocal):
    """str-->str
    OBJ: Cambia las vocales por los valores establecidos"""
    resultado=""
    if vocal=="a":
        resultado="4"

    elif vocal=="e":
        resultado="3"

    elif vocal=="i":
        resultado="1"

    elif vocal=="o":
        resultado="0"

    elif vocal=="u":
        resultado="#"

    return resultado

def Frase(cadena):
    """str-->str
    OBJ: introduce una cadena y cambia sus vocales"""
    FraseNueva=""
    for i in range(len(cadena)):
        if Vocales(cadena[i]):
            FraseNueva+=Vocales(cadena[i])
        else:
            FraseNueva+=cadena[i]
    return FraseNueva


print("La Frase nueva es esta: ",Frase("Probando si funciona correctamente"))

