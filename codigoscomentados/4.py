# Importar el módulo "random" de Python, que incluye funciones para generar números aleatorios.
import random

# Este bucle se ejecutará 10 veces, generando un número aleatorio en cada iteración.
for i in range(10):
    
    # La función "random()" devuelve un número aleatorio en el rango [0.0, 1.0).
    # Al multiplicar este valor por 100, se obtiene un número aleatorio en el rango [0.0, 100.0).
    # Finalmente, el valor se convierte en un número entero utilizando la función "int()".
    # El resultado es un número aleatorio entero en el rango [0, 99].
    random_number = int(random.random() * 100)
    
    # Imprimir el número aleatorio generado en esta iteración.
    print(random_number)
