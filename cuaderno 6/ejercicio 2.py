"Ejercicio 2"
 
def IntroduccionNumeros():
    """int,int-->int
    OBJ:Introduce dos numeros por teclado"""
    return int(input("introduzca el numero a multiplicar:"))

def multiplicacion(n1,n2):
    """int,int-->int
    OBJ:Introduce dos numeros y hace su multiplicacion"""
    suma=0
    for i in range(n2):
        suma+=n1
    return suma

#Probadores
numero1=IntroduccionNumeros()
numero2=IntroduccionNumeros()
print("La multiplicacion da como resultado: ",multiplicacion(numero1,numero2))