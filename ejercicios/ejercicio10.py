import random
n=int(input("Ingrese la longitdud de la lista: "))
def llenarlista(rango,tam=n):
    lista = [random.randrange(rango) for i in range(n)]
    return lista
def sumarlista(lista):
    sum=0
    for x in lista:
        sum += x
    return sum

def promediolista(lista):
    return sumarlista(lista)/len(lista)
l1=llenarlista(50)

def mayoraa(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo


resultado = mayoraa(l1)

def menor(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo
resultado2 = menor(l1)

listaasc=sorted(l1)
listades=sorted(l1, reverse=True)

def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista)//2] + lista[len(lista)//2-1])/2
    else:
        return lista[len(lista)//2]
mediana1=mediana(l1)

def media(lista):
    return sumarlista(lista)/len(lista)
media1=media(l1)

def moda(lista):
    lista.sort()
    return lista[len(lista)//2]

x=int(input("ingrese el numero que desea buscar: "))


print(l1)
print("La suma de la lista es: ",(sumarlista(l1)))
print("el promedio de la lista es:",(round(promediolista(l1),2)))
print("El valor máximo en la lista es:", resultado)
print("El valor minimo en la lista es:", resultado2)
print("la lista ordenada de manera ascendente es :",listaasc)
print("la lista ordenada de manera descente es :",listades)
print("la mediana de la lista es: ",mediana1)
print("la media de la lista es:",media1)
print("la moda de la lista es:",(moda(l1)))
