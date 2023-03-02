lista=[]
centinela=-1
cadena="murcielago"
cadena2=""

lista=list(cadena)

while centinela!="n":
    centinela=input("¿quiere cambiar algo de la lista?(s/n n es para cerrar): ")
    if centinela=="s":
        print()
        print(lista)
        for i in range(len(lista)):
            print(" ",i,end="  ")
        print()
        posicion=int(input("que posicion quieres elegir para cambiar: "))

        if posicion>len(lista)-1:
            print()
            print("SE HA EQUIVOCADO NO EXISTE ESA POSICION")
            print()

        else:
            print()
            caracter=input("Que caracter quiere poner: ")
            lista[posicion]=caracter
    else:
        print("Porfavor introduzca lo que se pide")

print()
print("Ha finalizado el programa con exito")

for i in lista:
    cadena2+=i

print("La palabra final ha sido esta: ",cadena2)