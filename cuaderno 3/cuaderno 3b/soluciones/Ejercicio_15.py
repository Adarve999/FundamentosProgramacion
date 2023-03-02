
import random

PALABRAS = ['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']

for i in range(5):
    frase = ''
    num_palabras = random.randint(3, 10)
    for j in range(num_palabras):
        palabra = PALABRAS[random.randint(0,len(PALABRAS)-1)]
        frase += palabra + ' '
    print(frase)
