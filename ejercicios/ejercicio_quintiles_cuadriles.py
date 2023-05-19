import random

tam = int(input("Ingrese la longitud de la lista: "))

def llenarlista(tam):
    lista = [round(random.uniform(1.50, 2.01), 2) for _ in range(tam)]
    return lista

l1 = llenarlista(tam)

def ordenarlista(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

print("Lista original:", l1)

ordenarlista(l1)

print("Lista ordenada:", l1)

def calcular_quintiles(lista):
    n = len(lista)
    indice_20 = int(n * 0.2)
    indice_40 = int(n * 0.4)
    indice_60 = int(n * 0.6)
    indice_80 = int(n * 0.8)
    quintil_20 = lista[indice_20]
    quintil_40 = lista[indice_40]
    quintil_60 = lista[indice_60]
    quintil_80 = lista[indice_80]
    return quintil_20, quintil_40, quintil_60, quintil_80, indice_20, indice_40, indice_60, indice_80

def calcular_cuartiles(lista):
    n = len(lista)
    indice_25 = int(n * 0.25)
    indice_50 = int(n * 0.5)
    indice_75 = int(n * 0.75)
    cuartil_25 = lista[indice_25]
    cuartil_50 = lista[indice_50]
    cuartil_75 = lista[indice_75]
    return cuartil_25, cuartil_50, cuartil_75, indice_25, indice_50, indice_75

quintil_20, quintil_40, quintil_60, quintil_80, indice_20, indice_40, indice_60, indice_80 = calcular_quintiles(l1)
cuartil_25, cuartil_50, cuartil_75, indice_25, indice_50, indice_75 = calcular_cuartiles(l1)

print("Quintil 20:", quintil_20)
print("Quintil 40:", quintil_40)
print("Quintil 60:", quintil_60)
print("Quintil 80:", quintil_80)
print("Índice del quintil 20:", indice_20)
print("Índice del quintil 40:", indice_40)
print("Índice del quintil 60:", indice_60)
print("Índice del quintil 80:", indice_80)

print("Cuartil 25:", cuartil_25)
print("Cuartil 50:", cuartil_50)
print("Cuartil 75:", cuartil_75)
print("Índice del cuartil 25:", indice_25)
print("Índice del cuartil 50:", indice_50)
print("Índice del cuartil 75:", indice_75)
