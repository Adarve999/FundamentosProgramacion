import math

"ejercicio 2"


def distancia_2D(x1,y1,x2,y2):
    """int,int,int,int-->float
    OBJ:Introduce las coordenadas de 2 puntos y calcula
        su distancia"""
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2)) 

print("la distancia es:",round(distancia_2D(1,2,4,5),3))