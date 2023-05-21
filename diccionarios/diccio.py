def d1():
    diccionario = {
        "Azalea": "Azalea",
        "Balsam": "Alegría",
        "Carnation": "Clavel",
        "Cherry_blossom": "Flor de cerezo",
        "Daffodil": "Narciso",
        "Dahlia": "Dalia",
        "Daisy": "Margarita",
        "Dandelion": "Diente de leon",
        "Jasmine": "Jazmín",
        "Lotus flores": "Flor de loto"
    }
    return diccionario

print(d1())

flowers = input("Ingrese la flor que desea buscar: ")

def buscar(flowers):
    if flowers in d1():
        print(flowers, "es", d1()[flowers])
    else:
        print(flowers, "no está en el diccionario")

buscar(flowers)
