"Ejercicio 6"

def Contar(numero):
    """int-->int
    OBJ: Introduce un numero y dice cuantos digitos tiene"""
    digitos=1
    divisible=False
    parteEntera=numero
    while not divisible:
        if parteEntera//10:
            parteEntera=numero//10
            digitos+=1
            divisible=True
    return digitos

#Probadores

print(Contar(100))
        
    