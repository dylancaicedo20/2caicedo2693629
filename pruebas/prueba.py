# Método 1: open()
archivo = open("archivo.txt", "r")  # Abre el archivo en modo lectura
contenido = archivo.read()  # Lee el contenido del archivo
print(contenido)
archivo.close()  # Cierra el archivo

# Método 2: with open()
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
