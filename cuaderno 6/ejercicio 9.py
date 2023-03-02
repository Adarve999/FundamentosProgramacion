 
"ejercicio 9"

def CreacionLista():
    """nothing-->list
    OBJ:Obtener una lista vacia para poder
        con ella"""
    return []

def InsertarAlumnos(lista,nombre,edad,titulacion):
    """str,int,str-->list
    OBJ:Introduce los 3 campos y lo mete en una lista"""
    alumno=[nombre,edad,titulacion]
    lista.append(alumno)
    return lista

def SumaEdades(lista):
    """lista-->int
    OBJ:Introduce la lista de los alumnos y suma recursivamente
        las edades de ellos"""
    edad=0
    for i in range(len(lista)-1,-1,-1): 
        edad+=lista[i][1]
    return edad


#Probadores
ListaDeAlumnos=CreacionLista()
InsertarAlumnos(ListaDeAlumnos,"ruben",22,"GISI")
InsertarAlumnos(ListaDeAlumnos,"Jorge",27,"GIF")
InsertarAlumnos(ListaDeAlumnos,"carlos",24,"GIC")
InsertarAlumnos(ListaDeAlumnos,"julio",20,"GIC")

print("         -LA LISTA DE ALUMNOS-")
print(ListaDeAlumnos)
print("la suma de las edades es: ",SumaEdades(ListaDeAlumnos))