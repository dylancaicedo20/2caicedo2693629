#se importa la funcion random
import random
#se define la funcion llenarlista
def llenarlista(tam,rango):
    lista = [random.randrange(rango) for i in range(tam)]
    return lista
#se define la funcion sumarlista
def sumarlista(lista):
    sum=0
    for x in lista:
        sum += x
    return sum
#se define la funcion promediolista
def promediolista(lista):
    return sumarlista(lista)/len(lista)
#se imprimen los resultados
l1=llenarlista(10,50)
print(sumarlista(l1))
print(l1)
print(round(promediolista(l1),2))