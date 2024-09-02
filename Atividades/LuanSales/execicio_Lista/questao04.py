numero1 = 1
# Números de 1 a 10
while numero1 <= 10:
    numero2 = 1
    print(f"=> Tabuada do {numero1}:")

    # While para realizar a multiplicação
    while numero2 <= 10:
        resultado = numero1 * numero2
        print(f"{numero1} x {numero2} = {resultado}")
        numero2 += 1
    numero1 += 1