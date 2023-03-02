
"ejercicio 13"

def es_float(n):
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    return resultado


kilometros=input("Introduzca los Kilometros del vehiculo: ")

if es_float(kilometros):
    kilometros=float(kilometros)

    if kilometros < 300:
        print("La factura ha dado como resultado 100€")

    elif 300 <= kilometros <= 1000:
        factura=((kilometros-300)*0.30)+100
        print("Por",kilometros,"km, El valor de la factura de este caso es de:   ",factura,"€")

    elif kilometros > 1000:
        factura=((700*0.30)+((kilometros-1000)*0.20))+100
        print("Por",kilometros,"km, El valor de la factura de este caso es de:   ",factura,"€")
else:
    print("No ha introducido correctamente el valor de los kilometros")