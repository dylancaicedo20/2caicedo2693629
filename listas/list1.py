# Definimos una variable llamada x y le asignamos el valor 100
x = 100

# Imprimimos el tipo de la variable x usando la función type()
print('tipo de x',type(x))

# Definimos una lista llamada lista con diferentes tipos de elementos
lista = [1, 1.4, 'sena', ['a', 'b'], 'soacha']

# Imprimimos el quinto elemento de la lista, que en este caso es la palabra 'soacha'
print(f'elemento {lista[4]}')

# Imprimimos la longitud de la lista usando la función len()
print(len(lista))

# Imprimimos el tipo de la variable lista usando la función type()
print('tipo de lista',type(lista))

# Imprimimos el último elemento de la lista usando el índice -1
print('ultimo indice',lista[-1])

# Imprimimos de nuevo la longitud de la lista (no es necesario hacerlo dos veces)
print(len(lista))

# Agregamos el número 20 al final de la lista usando el método append()
lista.append(20)

# Agregamos la palabra 'python' al final de la lista usando el método append()
lista.append('python')

# Imprimimos la lista actualizada con los dos nuevos elementos
print(lista)

# Insertamos la palabra 'java' en la última posición de la lista usando el método insert()
# Es equivalente a lista.append('java') ya que insert(len(lista),'java') indica que queremos insertar 'java' en la última posición
lista.insert(len(lista),'java')

# Imprimimos la lista actualizada con el nuevo elemento 'java'
print(lista)
