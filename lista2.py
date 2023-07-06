def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
            print(f"Valor aceptado: {lista}")
    except ValueError as error:
        print(error)
    finally:
        print("Gracias por usar este programa.")

numeros = [4, 7, 6, 8, 9]
while True:
    try:
        nuevo = int(input("Escriba un número: "))
        agregar_una_vez(numeros, nuevo)
        break
    except KeyboardInterrupt:
        print("Se interrumpió la ejecución.")
