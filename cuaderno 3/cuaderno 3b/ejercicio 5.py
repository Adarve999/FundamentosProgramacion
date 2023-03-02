
"ejercicio 5"

def dibujar_rectangulo(a,b,pares,impares):
    """ int,int,str -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones
    a por b utilizando el símbolo como relleno
    """
    for i in range(1,a):
        for j in range(b):
            if i%2==0:
                print(pares,end="  ")
            else:
                print(impares,end="  ")
        print()

def dibujar_rectangulo2(a,b,pares,impares):
    """ int,int,str -> None
    OBJ: Dibuja en pantalla un rectángulo de dimensiones
    a por b utilizando el símbolo como relleno
    """
    for i in range(a):
        for j in range(1,b):
            if j%2==0:
                print(pares,end=" ")
            else:
                print(impares,end=" ")
        print() 

print("APARTADO 3a ")
dibujar_rectangulo(10,20,"@","#")

print("APARTADO 3b")
dibujar_rectangulo2(10,20,"@","#")
            