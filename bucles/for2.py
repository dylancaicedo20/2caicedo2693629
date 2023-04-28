p = int(input('Ingrese un número positivo: '))
while p < 0:
    p = int(input('El número ingresado es negativo. Ingrese un número positivo: '))    

n = int(input('Ingrese un número del cual quiera saber los múltiplos: '))

count = 0
for i in range(p + 1):
    if i % n == 0:
        count += 1

print(f"Hay {count} múltiplos de {n} en la serie desde cero hasta {p}.")
