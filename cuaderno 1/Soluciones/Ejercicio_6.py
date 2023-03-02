"""
Cuaderno de trabajo 1.pdf - Ejercicio 6:

Descripción: Contabilidad de camiones
"""

# Programa principal
distancia = float(input('Introduzca la distancia recorrida (km): '))
litros = float(input('Introduzca la cantidad de combustible usada (l): '))
precio = float(input('Introduzca el precio del combustible (€/l): '))
mantenimiento = float(input('Introduzca el coste de mantenimiento (€): '))

km_litro = distancia / litros
coste_total = (litros * precio) + mantenimiento
coste_km = coste_total / distancia

print(f'Kilómetros recorridos por litro: {km_litro:.2f} km/l')
print(f'Coste total del viaje: {coste_total:.2f} €')
print(f'Coste por kilómetro: {coste_km:.2f} €')
