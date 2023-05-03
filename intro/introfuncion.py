# Importamos los módulos math y random
import math
import random

# Utilizamos la función sqrt del módulo math para obtener la raíz cuadrada de 100
print(math.sqrt(100))

# Utilizamos la función pow del módulo math para elevar 2 a la potencia de 5
print(math.pow(2,5))

# Generamos un número aleatorio entre 0 y 100 utilizando random.random
# y lo convertimos a entero utilizando int
num=int(random.random()*100)
print(num)

# Generamos un número aleatorio entero entre 10 y 20 utilizando random.randint
num1=random.randint(10,20)
print(num1)

# Definimos una función llamada saludo que toma un parámetro llamado nombre
def saludo(nombre):
    return f'Hola {nombre}'

# Llamamos a la función saludo con el argumento 'Soacha' y almacenamos el resultado en la variable var
var=saludo('Soacha')

# Utilizamos la función len para obtener la longitud de la cadena almacenada en la variable var
print(len(var))

# Imprimimos el valor almacenado en la variable var
print(var)

# Llamamos a la función saludo con diferentes argumentos
saludo('Maria')
saludo('Pedro')
saludo('Ana')
