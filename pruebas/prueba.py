<<<<<<< HEAD
from math import *
from math import sqrt, pi, sin
import math as m
import numpy as np

print(np.sin(np.pi/2))


# Utilizando la función sqrt (raíz cuadrada)
x = 16
raiz_cuadrada = sqrt(x)
print("La raíz cuadrada de", x, "es:", raiz_cuadrada)

# Utilizando la constante pi
radio = 5
area_circulo = pi * radio ** 2
print("El área del círculo con radio", radio, "es:", area_circulo)

# Utilizando la función sin (seno)
angulo = 45
seno_angulo = sin(angulo)
print("El seno de", angulo, "grados es:", seno_angulo)

=======
# Método 1: open()
archivo = open("archivo.txt", "r")  # Abre el archivo en modo lectura
contenido = archivo.read()  # Lee el contenido del archivo
print(contenido)
archivo.close()  # Cierra el archivo

# Método 2: with open()
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
>>>>>>> 10644f1149074537a6c506f64c2eb3284bcd5727
