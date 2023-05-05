import random

lista = []
tam = random.randint(15, 20)


for i in range(tam):
    lista.append(random.randint(0,9))
print(lista)
x = int(input("Ingrese el numero a buscar: "))
if x in lista:
    print("El numero si esta en la lista")
if not x in lista:
    print ("El numero no esta en la lista")
contador = 0
for numero in lista:
    if numero == x:
        contador += 1
print(f"El número {x} aparece {contador} veces en la lista {lista}")
