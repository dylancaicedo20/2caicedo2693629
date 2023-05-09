num = int(input("Ingrese un número positivo: "))
while num < 0:
    num = int(input("El número ingresado es negativo. Ingrese un número positivo: "))

n = int(input("Ingrese el valor de n: "))

count = 0
for i in range(num + 1):
    if i % n == 0:
        count += 1

print(f"Hay {count} múltiplos de {n} en la serie desde cero hasta {num}.")
