"""
Cuaderno de trabajo 1.pdf - Ejercicio 7:

Descripción: Conversor de distancias
"""

# Programa principal
km = float(input('Introduzca una distancia (km): '))

m = km * 1000
dm = m / 10
hm = m / 100

print(f'Distancia en hectómetros: {hm:.2f} hm')
print(f'Distancia en decámetros: {dm:.2f} dm')
print(f'Distancia en metros: {m:.2f} m')
