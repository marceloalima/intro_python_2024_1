cont = 0
soma = 0

# Lendo os 10 números
while cont < 10:
    num = int(input('Digite um número: '))

    # Efetuando a soma 
    if num < 40: # Inferior a 40
        soma = soma + num
    cont += 1
print(f'A soma dos números inferiores a 40 é: {soma}')