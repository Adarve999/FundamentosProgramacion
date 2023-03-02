"""
Cuaderno de trabajo 1.pdf - Ejercicio 14:

Descripción: Conversor Euros a Libras
"""

euros = float(input('Introduce la cantidad en euros: '))
tipo_cambio = float(input('Introduce el tipo de cambio: '))

libras = euros * tipo_cambio
comision = (libras * 2) / 100
cambio = libras - comision

print (f'{euros} euros son {libras:.2f} libras')
