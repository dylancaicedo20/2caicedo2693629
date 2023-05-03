# Inicializar las variables "num", "cont", "sum", "mayor" y "menor".
num = 1
cont = 0
sum = 0
mayor = 0
menor = 1000000

# Este bucle "while" se ejecutará mientras que "num" sea diferente de cero.
# En cada iteración, se le pedirá al usuario que ingrese un número utilizando la función "input()".
# La variable "cont" se incrementará en uno, la variable "sum" se actualizará sumando el número ingresado,
# y las variables "mayor" y "menor" se actualizarán si el número ingresado es mayor o menor que los valores actuales,
# respectivamente. El bucle terminará cuando se ingrese un cero como entrada.
while num != 0:
    num = int(input('Ingrese un número: '))
    cont = cont + 1
    sum = sum + num
    if num > mayor:
        mayor = num
    if num < menor and num != 0:
        menor = num

# Al final del bucle, se imprimirán las estadísticas sobre los números ingresados por el usuario.
print(f'El usuario ingresó {cont-1} números') # Se resta 1 del contador para no contar el cero final.
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}') # Se divide la suma entre la cantidad de números ingresados (sin contar el cero final).
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
