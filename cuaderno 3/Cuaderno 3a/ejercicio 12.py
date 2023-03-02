
"ejercicio 12"

import math

opcion=-1

while opcion!=0:

    print('\t 1. Seno')
    print('\t 2. coseno')
    print('\t 3. Tangente')
    print('\t 4. Cotangente')
    print('\t 5. Secante')
    print('\t 6. Cosecante')
    print('\t 0. Salir')
    try:
        opcion=int(input("\t Que operacion desea usar:    "))
    except:
        print("\t       __________________________________")
        print("\t       OPCION NO VALIDA, repita la opcion")
        print("\t       ----------------------------------")
    else:
        if 1<= opcion <= 6:
            try:
                angulo=float(input("Introduzca el valor del angulo (en radianes): "))
            except:
                print("Lo introducido no corresponde con el campo del angulo")
            else:
                if opcion==1: 
                    print("El seno es, ",math.sin(angulo))
                elif opcion==2: 
                    print("El coseno es, ",math.cos(angulo))
                elif opcion==3: 
                    print("El tangente es, ",math.tan(angulo))
                elif opcion==4: 
                    print("la cotangente es, ",math.atan(angulo))
                elif opcion==5: 
                    print("La secante es, ",1/math.cos(angulo))
                elif opcion==6: 
                    print("La cosecante es, ",1/math.sin(angulo))
