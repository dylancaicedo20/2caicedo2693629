# Inicializar una variable "i" con el valor 1 y otra variable "sum" con el valor 0.
i = 1
sum = 0

# Este bucle "while" se ejecutará mientras "i" sea menor o igual a 10.
# En cada iteración, se imprimirá el valor de "i", se añadirá "i" a "sum", y se aumentará "i" en 1.
while i <= 10:
    print(i)
    sum += i # Es lo mismo que decir: sum = sum + i
    i += 1 # Es lo mismo que decir: i = i + 1

# Después de que termine el bucle, se imprimirá el mensaje "la suma es:" seguido del valor de "sum".
print('la suma es:', sum)

# Inicializar una variable "i" con el valor 0, y dos variables "sp" y "si" con el valor 0.
i = 0
sp, si = 0, 0

# Este bucle "while" se ejecutará mientras "i" sea menor o igual a 10.
# En cada iteración, se imprimirá el valor de "i", y si "i" es par se añadirá a "sp", y si es impar se añadirá a "si".
# Al final de cada iteración, se aumentará "i" en 1.
while i <= 10:
    print(i)
    if i % 2 == 0:
        sp += i
    else:
        si += i
    i += 1

# Después de que termine el bucle, se imprimirán dos mensajes: "la suma de los pares es:" seguido del valor de "sp",
# y "la suma de los impares es:" seguido del valor de "si".
print('la suma de los pares es:', sp)
print('la suma de los impares es:', si)
