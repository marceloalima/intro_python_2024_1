dentro = 0
fora = 0
cont = 0
while cont < 10:
    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20:
        # Valores de dentro
        dentro += 1
    else:
        # Valores de fora
        fora += 1
    cont += 1
print(f"{dentro} números estão entre 10 e 20")
print(f"{fora} números estão fora de 10 e 20")
