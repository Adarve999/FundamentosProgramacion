
"AGENDA"

def new_agenda():
    """lista-->lista
    OBJ:devuelve una lista vacia"""
    lista=[]
    return lista

def find_phone(lista,nombre):
    """lista,nombre-->bool
    OBJ: Introduce la lista y el nombre y dice el numero de la persona"""
    encontrado=False 
    for i in range(len(lista)):
        for r in range(len(lista[i])):
            if nombre==lista[i][r]:
                encontrado=True
                telefono=lista[i][1]              
    if not encontrado:
        print("None")
    else:
        print("el telefono de",nombre,"es: ",telefono)

def add_entry(lista,nombre,telefono):
    """lista,nombre,numero,bool-->lista
    OBJ:Introduce un usuario en la agenda y verifica si esta repetido o no"""
    contacto=[nombre,telefono]
    lista.append(contacto)  

def delete_entry(lista,nombre):
    """lista,nombre-->bool
    OBJ: Introduce la lista y el nombre e elimina el contacto"""
    encontrado=False
    for i in range(len(lista)-1,-1,-1):
        for r in range(len(lista[i])-1,-1,-1):
            if nombre in lista[i][r]:
                lista.pop(i)
                encontrado=True
    if not encontrado:
        print(nombre, "no aparece en la agenda por ninguna parte.")
    else:
        print(nombre,"se ha eliminado correctamente.")
    
#Nueva agenda
agenda=new_agenda()

#Introduccion de contactos
add_entry(agenda,"carlos","693303639")
add_entry(agenda,"pepe","693303459")
add_entry(agenda,"juan","323303459")
add_entry(agenda,"jose","123303459")
add_entry(agenda,"julio","1231231")
print(agenda)

#busqueda de contactos
find_phone(agenda,"pepe")
find_phone(agenda,"pepito")
find_phone(agenda,"jose")

#eliminacion de algun contacto de la agenda
delete_entry(agenda,"jose")
print(agenda)
delete_entry(agenda,"ruben")