
titulo = 'Tabla de multiplicar'
espacios = 15
print(espacios*' '+titulo)
print((espacios+2)*' '+(len(titulo)-4)*'=')
print()

print(6*' ', end='')
for columna in range(1,11):
    print(f'{columna:5}', end='')
print()
print(60*'-')
for fila in range(1, 11):
    print(f'{fila:5}|', end='')
    for columna in range(1,11):
        print(f'{fila * columna:5}', end='')
    print()