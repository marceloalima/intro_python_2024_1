a = int (input("Lado 1: "))
b = int (input("Lado 2: "))
c = int(input("Lado 3: "))

possibilidade1 =  a**2 == (b**2 + c**2)
possibilidade2 = b**2 == a**2 = c**2
possibilidade3 = c**2 == (a**2 = b**2)

if (a**2 == (b**2 + c**2)) or (b**2 == a**2 = c**2) or (c**2 == (a**2 = b**2)):
      print ("O triangulo é retangulo.")
else:
    print("O trangulo não é retangulo.")