a = int(input("Entre com o primeiro lado do triângulo: "))
b = int(input("Entre com o segundo lado do triângulo: "))
c = int(input("Entre com o terceiro lado do triângulo: "))

possibilidade1 = a**2 == (b**2 + c**2)
possibilidade2 = b**2 == (a**2 + c**2)
possibilidade3 = c**2 == (a**2 + b**2)

if possibilidade1 or possibilidade2 or possibilidade3:
    print("O Triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")