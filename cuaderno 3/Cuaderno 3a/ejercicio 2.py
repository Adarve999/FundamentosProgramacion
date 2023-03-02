
"ejercicio 2"

def Hora_valida(n):
    return 0<= n <= 24

def minutos_validos(n):
    return 0<= n <= 59

Hora=int(input("introduce la hora:  "))

if Hora_valida(Hora):
    minuto=int(input("introduce los minutos:    "))
    if minutos_validos(minuto):
        if Hora <= 12:
            print("La hora nueva es:    ",Hora,":",minuto,"AM")
        else:
            Hora_Nueva=Hora-12
            print("La hora nueva es:    ",Hora_Nueva,":",minuto,"PM")
    else:
        print("Has introducido mal los minutos")
else:
    print("Has introducido mal la Hora")
