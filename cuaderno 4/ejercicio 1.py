def square(numbers):
    for i in range(len(numbers)):
        numbers[i]= numbers[i]**2

L=list(range(11))
square(L)
print(L)

def square2(numbers):
    for i in range(len(numbers)):
        if numbers[i]<0:
            numbers[i]=0

j=[0,2,12,-1,-3,6,7,-9]
square2(j)
print(j)

print()

def matriz(n):
    row=[0]*n
    m=[]
    for i in range(n):
        m.append(row.copy())
    return m

def printmatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

printmatriz(matriz(5))
