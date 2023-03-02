
"ejercicio 1"

def es_real_valido(n):
    """?-->bool
    OBJ: devolver verdadero si el parametro es conmvertible a real."""
    try:
        float(n)
    except:
        resultado=False
    else:
        resultado=True
    return (resultado)

def validar_tipo_pago(tipo):
    """string-->bool
    OBJ: devuelve true si el tipo de pago es valido (t / e )"""
    if tipo=="t" or tipo=="e":
        resultado=True
    else:
        resultado=False
    return (resultado)

desc_tarjeta=0.02
desc_efectivo=0.05

importe_compra=input("introduzca el importe de la compra:")


if es_real_valido(importe_compra):
    importe_compra=float(importe_compra)
    tipo_pago=input("tarjeta o efectivo (t / e ):")

    if validar_tipo_pago(tipo_pago):   #Comprueba el tipo de pago
        if (importe_compra>=100):
            if tipo_pago=="t":
                importe_final=importe_compra-(importe_compra*desc_tarjeta)
            else:
                importe_final=importe_compra-(importe_compra*desc_efectivo)
        else:
            importe_final=importe_compra
        print("total a pagar:   ",importe_final)
    else:
        print("el tipo de pago es incorrecto")

else:
    print("el valor de la compra introducido no es valido")