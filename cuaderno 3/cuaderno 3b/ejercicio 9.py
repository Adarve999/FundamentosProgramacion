
"ejercicio 9"

ROMANOS = ['M','D','C','L','X','V','I']
VALORES = [1000,500,100,50,10,5,1]
n = 600  # 1<=arabigo<=3999
romano = ''
pos = 0
while n > 0:
    cuantos = n // VALORES[pos]
    n = n % VALORES[pos]
    if cuantos <= 3:
        romano += ROMANOS[pos] * cuantos
    elif len(romano)>0 and romano[-1]==ROMANOS[pos-1]:
        romano = romano[:-1] + ROMANOS[pos] + ROMANOS[pos-2]
    else:
        romano = romano + ROMANOS[pos] + ROMANOS[pos-1]
    pos += 1

print(romano)