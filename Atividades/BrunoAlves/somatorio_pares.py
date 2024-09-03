inicio = int(input("Digite o valor do inicio: "))
fim = int(input("Digite o valor do fim: "))

while inicio <= fim:
    if inicio % 2 == 0:
        print(inicio)
    inicio = inicio + 1

# somatorio dos impares

inicio = int(input("Digite o valor do inicio: "))
fim = int(input("Digite o valor do fim: "))

while inicio <= fim:
    if inicio % 2 != 0:
        print(inicio)
    inicio = inicio + 1