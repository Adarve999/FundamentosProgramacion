
"ejercicio 3"

def IntroduccionNumeros():
    """int,int-->int
    OBJ:Introduce dos numeros por teclado"""
    return int(input("introduzca el numero a dividir:"))

def division(n1,n2):
    """int,int-->int
    OBJ:Introduce dos numeros y hace su multiplicacion"""
    cocciente=0
    while n1!=0 and n1>=n2:
        n1=n1-n2
        cocciente+=1
    return cocciente

#Probadores
numero1=IntroduccionNumeros()
numero2=IntroduccionNumeros()
print("La division da como resultado: ",division(numero1,numero2))