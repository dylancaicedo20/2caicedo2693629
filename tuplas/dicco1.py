d1={"rojo": "red",
    "amarillo":"yellow",
    "azul":"blue",
    "verde":"green",
    "cafe":"brown",
    "blanco":"white",
    "naranja":"oranje",
    "negro":"black",
    "gris":"grey",
    "morado":"purple" }

colors=["rojo", "negro", "gris","gold"]

for color in colors:
    if color in d1:
        print(color, "es", d1[color])
    else:
        print(color, "no esta en el diccionario")