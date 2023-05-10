# Inicializar dos variables "x" e "y" con los valores 5 y 3, respectivamente.
x = 5
y = 3

# Este bucle "while" se ejecutará mientras que ni "x" sea divisible por "y" ni "y" sea divisible por "x".
# En cada iteración, se imprimirá un mensaje "Rutina para saber si dos numeros son factores",
# y se pedirá al usuario que ingrese dos números nuevos para "x" e "y" utilizando la función "input()".
# Si "x" es divisible por "y" o "y" es divisible por "x", el bucle se detendrá.
while not (x % y == 0 or y % x == 0):
    print('Rutina para saber si dos numeros son factores')
    x = int(input('Ingrese un número: '))
    y = int(input('Ingrese otro número: '))
    
# Después de que el bucle termine, se imprimirá el mensaje "Son factor".
print('Son factor')