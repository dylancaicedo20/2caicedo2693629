# Se le pide al usuario que ingrese dos números y se almacenan en las variables "x" e "y".
x = input('Ingrese un número: ')
y = input('Ingrese otro número: ')

# Se utiliza una estructura "if-elif-else" para determinar si los números son iguales, ascendentes o descendentes.
if x == y:
    print('Los números son iguales')
elif x > y:
    print('Los números están en orden descendente')
else:
    print('Los números están en orden ascendente')
