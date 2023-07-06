lista = []

while True:
    try:
        print("----- MENÚ -----")
        print("1. Cargar una lista Python (solo nombres en mayúsculas y del grupo 2693629)")
        print("2. Mostrar la lista Python")
        print("3. Elegir una posición de la lista")
        print("-----------------")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre = input("Ingrese un nombre: ")
            if nombre.isupper() and nombre in ["LAURA", "HAROL", "ERICK", "JUAN", "ZAIR", "JESSICA", "CESAR", "BRAYAN", "AREVALO", "SEBASTIAN", "LUISA", "DIEGO", "DYLAN", "DANIELA"]:
                if nombre not in lista:
                    lista.append(nombre)
                    print("Nombre agregado correctamente.")
                else:
                    print("El nombre ya existe en la lista.")
            else:
                print("El nombre no está en mayúsculas o no es del grupo 2693629. No se agregará a la lista.")

        elif opcion == 2:
            print("Contenido de la lista:")
            print(lista)

        elif opcion == 3:
            posicion = int(input("Ingrese una posición de la lista: "))
            if posicion < 0 or posicion >= len(lista):
                raise IndexError("Error: Posición inexistente en la lista.")
            else:
                valor = lista[posicion]
                print("El valor en la posición", posicion, "es:", valor)

        else:
            print("Opción inválida. Ingrese nuevamente.")

    except ValueError:
        print("Error: Ingrese un número válido como opción.")
    except IndexError as error:
        print(error)

    finally:
        print("Gracias por usar este programa.")

