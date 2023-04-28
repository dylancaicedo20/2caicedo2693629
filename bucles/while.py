mayor = float('-inf')
menor = float('inf')
resta=0
resta1=0
while True:
    x = int(input('Ingrese un numero: '))
    if x == 0:
        break
    y = int(input('Ingrese un numero: '))
    if y == 0:
        break
    if x > mayor:
        mayor = x
    if y > mayor:
        mayor = y
    if x < menor:
        menor = x
    if y < menor:
        menor = y
    if x==y:
        x = int(input('Ingrese otro numero: ')) 
    if y==x:
        y = int(input('Ingrese otro numero: '))
    if x == 0:
        break
    if y == 0:
        break

    print(f'El numero mayor fue: {mayor}')
    print(f'El numero menor fue: {menor}')

    while x > y:
        resta=x-y
    print('la resta es: ',resta)

    while y > x:
            resta1=y-x
    print('la resta es: ',resta1)
    print('el programa a terminado')