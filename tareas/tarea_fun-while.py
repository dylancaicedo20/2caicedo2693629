def imprimir_multiplos_de_cinco(N):
    i = 1
    while i <= N:
        if i % 5 == 0:
            print(i)
        i += 1

N = int(input("Introduce el número máximo: "))
imprimir_multiplos_de_cinco(N)
