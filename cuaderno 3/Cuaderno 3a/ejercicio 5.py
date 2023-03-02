"Ejercicio 5"

def validar_calificacion(n):
    """?-->Float
    OBJ: Introduce la nota y dice si es float o no"""
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado

def Nota_A(n):
    return 8.5 <= n <=10

def Nota_B (n):
    return 6.5 <= n < 8.5

def Nota_C (n):
    return 5 <= n < 6.5

def Nota_D (n):
    return 3.5 <= n < 5

def Nota_F (n):
    return  n < 3.5  

Calificacion=input("Introduzca la calificacion: ") 

if validar_calificacion(Calificacion):
    Calificacion=float(Calificacion)

    if Nota_A(Calificacion):
        print("enhorabuena tu nota es,",Calificacion, "  ,una A")

    elif Nota_B(Calificacion):
        print("enhorabuena tu nota es,",Calificacion, "  ,una B")

    elif Nota_C(Calificacion):
        print("enhorabuena tu nota es,",Calificacion, "  ,una C")

    elif Nota_D(Calificacion):
        print("enhorabuena tu nota es,",Calificacion, "  ,una D") 

    elif Nota_F(Calificacion):
        print("enhorabuena tu nota es,",Calificacion, "  ,una F")  

else:
    print("Ha introducido otro valor que no es un float")