
"ejercicio 4"

def validar_entero(n):
    """?-->int
    OBJ: introduzca algo y que verifique cual es entero"""
    try:
        int (n)
    except:
        resultado=False
    else:
        resultado=True

    return resultado

def Hora_valida(n):         #validacion del rango de la HORA
    return 0<= n <= 24

def minutos_validos(n):     #validacion del rango de los MINUTOS
    return 0<= n <= 59

Hora=input("introduce la hora:  ")

if validar_entero(Hora):              #VALIDAMOS SI ES ENTERO LA HORA  
    Hora=int(Hora)

    if Hora_valida(Hora):
        minuto=input("introduce los minutos:    ")

        if validar_entero(minuto):           #VALIDAMOS SI ES ENTERO LOS MINUTOS
            minuto=int(minuto) 

            if minutos_validos(minuto):
                if Hora <= 12:
                    print("La hora nueva es:    ",Hora,":",minuto,"AM")
                else:
                    Hora_Nueva=Hora-12
                    print("La hora nueva es:    ",Hora_Nueva,":",minuto,"PM")
            else:
                print("Se nos ha ido de rango los minutos")
        else:
            print("los minutos introducidos no son de tipo entero")
    else:
        print("se nos ha ido de rango la Hora")
else:
    print("La hora introducida no es de tipo real")
