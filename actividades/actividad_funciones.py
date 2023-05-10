import random
def llenarlista(tam,rango):
    lista = [random.randrange(rango) for i in range(tam)]
    return lista
def sumarlista(lista):
    sum=0
    for x in lista:
        sum += x
    return sum

def promediolista(lista):
    return sumarlista(lista)/len(lista)
l1=llenarlista(10,50)
print(sumarlista(l1))
print(l1)
print(round(promediolista(l1),2))