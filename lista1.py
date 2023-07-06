lista = [3, 5, 6, 8, 8, 6, 4, 5, 66, 777, 3, 3, 3, 5, 6, 5]

while True:
    try:
        pos = int(input("Ingresa la posición del elemento que deseas obtener: "))
        valor = lista[pos]
        print(f"El valor en la posición {pos} es {valor}")
        break
    except ValueError:
        print("Error: Ingresa una posición válida (número entero).")
    except IndexError:
        print("Error: La posición ingresada está fuera del rango de la lista.")
