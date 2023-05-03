# Importamos el módulo random
import random

# Creamos una lista vacía llamada "lista"
lista=[]

# Generamos un número aleatorio entero entre 10 y 20 inclusive y lo guardamos en la variable "tam"
tam=int(random.randint(10,20))

# Imprimimos el valor de "tam" en la consola
print(tam)

# Generamos un bucle "for" que se ejecuta "tam" veces
for i in range(tam):
    # Generamos un número aleatorio entero entre 0 y 99 inclusive y lo guardamos en la variable "num"
    num=int(random.randrange(100))
    # Añadimos "num" a la lista "lista" usando el método append()
    lista.append(num)

# Imprimimos la lista final en la consola
print(lista)
