# Se definen dos variables numéricas.
num1, num2 = 100, 25

# Se imprime un menú con las opciones de operaciones que se pueden realizar.
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')

# Se solicita al usuario que seleccione una opción del menú.
selector = (input('Digite la opción: '))

# Se utiliza una estructura "match-case" para seleccionar la opción elegida por el usuario y realizar la operación correspondiente.
match selector:
    case '1':
        print(num1 + num2) # Suma de num1 y num2
    case '2':
        print(num1 - num2) # Resta de num1 y num2
    case '3':
        print(num1 * num2) # Multiplicación de num1 y num2
    case '4':
        print(num1 / num2) # División de num1 entre num2
