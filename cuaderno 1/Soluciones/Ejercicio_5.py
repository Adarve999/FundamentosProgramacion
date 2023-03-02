"""
Cuaderno de trabajo 1.pdf - Ejercicio 5:

Descripción: Calcular segundos desde y hasta medianoche
"""

# Programa principal
horas = int(input('Introduce las horas: '))
minutos = int(input('Introduce los minutos: '))
segundos = int(input('Introduce los segundos: '))

# Segundos
seg_desde = horas * 3600 + minutos * 60 + segundos
seg_hasta = (24 * 3600) - seg_desde

print(f'Segundos transcurridos desde medianoche: {seg_desde}')
print(f'Segundos transcurridos hasta la siguiente medianoche: {seg_hasta}')
