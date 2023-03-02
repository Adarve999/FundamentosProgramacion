
"ejercicio 1"

def insercion():
    """nothing-->list
    OBJ:inserta datos en el nuevo diccionario
        pero cada informacion de una persona se introduce en una lista"""
    lista=[]
    stop=-1
    while stop!="999":
        nombre=input("Introduzca el nombre de la persona:")
        sexo=input("Introduzca el sexo (H / M ):")
        edad=int(input("Introduzca la edad de la persona:"))
        
        dic={'nombre':nombre,'sexo':sexo,'edad':edad}
        lista.append(dic)
        
        stop=input("introduzca (s) para seguir o (999)para dejar de insertar:")
    print("La agenda queda así:",lista)
    return lista
        
def lectura(lista,nombre):
    """introduce el nombre de la persona y dice si esta o no
       y ademas muestra sus datos"""
    for i in range(len(lista)):
        if lista[i]['nombre']==nombre:
            print("si se encuentra.")
            print("El sexo es:",lista[i]['sexo']," ,La edad es: ",lista[i]['edad'])
        else:
            print("No se encuentra dentro del diccionario")

#Probadores

contactos=insercion()

lectura(contactos,"ruben")