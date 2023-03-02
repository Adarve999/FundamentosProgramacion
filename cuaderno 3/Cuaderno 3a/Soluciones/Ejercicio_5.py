"""
Cuaderno de trabajo 3a.pdf - Ejercicio 5:
"""

def nota_a_texto(nota):
    """ float --> str
    OBJ: convierte una nota en formato decimal 0-10 a una escala A-F
    """
    nota_text = 'fuera de rango'
    if 0 <= nota <= 10:
        if nota >= 8.5:
            nota_text = 'A'
        elif nota >= 6.5:
            nota_text = 'B'
        elif nota >= 5:
            nota_text = 'C'
        elif nota >= 3.5:
            nota_text = 'D'
        else:
            nota_text = 'F'
    return nota_text

# Programa principal
try:
    mi_nota = float(input('Introduce una nota: '))
except:
    print('Error: no es un número')
else:
    print(f'La nota es: {nota_a_texto(mi_nota)}')
