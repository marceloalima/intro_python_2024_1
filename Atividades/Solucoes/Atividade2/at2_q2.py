numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print(numero1, "é maior que", numero2)
elif numero2 > numero1:
    print(numero2, "é maior que", numero1)
else:
    print(numero1, "é igual a", numero2)