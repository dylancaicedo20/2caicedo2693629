import random

lista = []
tam = random.randint(10, 20)

# Generar números aleatorios
for i in range(tam):
  lista.append(random.randint(1, 100))

suma = sum(lista)
mayor = max(lista)
menor = min(lista)

# Ordenar la lista
lista = sorted(lista)

# Calcular la mediana
if tam % 2 == 0:
  mediana = (lista[tam // 2 - 1] + lista[tam // 2]) / 2
else:
  mediana = lista[tam // 2]

# Calcular la media
media = suma / tam

# Calcular la desviación estándar
desv = 0
for num in lista:
  desv += (num - media)**2
desv = (desv / (tam - 1))**0.5

# Calcular la moda
contador = {}
for num in lista:
  if num in contador:
    contador[num] += 1
  else:
    contador[num] = 1
moda = max(contador, key=contador.get)

# Imprimir resultados
print(f"La lista es: {lista}")
print(f"El tamaño de la lista es: {tam}")
print(f"La suma es: {suma}")
print(f"El promedio es: {media}")
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
print(f"La mediana es: {mediana}")
print(f"La desviación estándar es: {desv}")
print(f"La moda es: {moda}")