"""
Cuaderno de trabajo 3a.pdf - Ejercicio 14:
"""

def baremacion_escuelas_infantiles(ingresos):
    """ float --> int
    OBJ: Indica el número de puntos en el baremo según ingresos
    """
    puntos = -1
    if ingresos >= 5000:
        puntos = 1
    elif ingresos >= 3500:
        puntos = 2
    elif ingresos >= 1000:
        puntos = 3
    elif ingresos >= 0:
        puntos = 4
    return puntos


# Probador
print(f"{baremacion_escuelas_infantiles(5000)}")
print(f"{baremacion_escuelas_infantiles(3500)}")
print(f"{baremacion_escuelas_infantiles(1800)}")
print(f"{baremacion_escuelas_infantiles(0)}")