#Q1#
# Entrada dos comprimentos dos lados do triângulo
a = float(input("Informe o comprimento do lado A: "))
b = float(input("Informe o comprimento do lado B: "))
c = float(input("Informe o comprimento do lado C: "))

# Verificar se o triângulo é equilátero
if a == b == c:
    print("O triângulo é equilátero!")
else:
    print("O triângulo não é equilátero.")

#Q2#
#Entrada dos comprimentos dos lados do triângulo
a = float(input("Informe o comprimento do lado a: "))
b = float(input("Informe o comprimento do lado b: "))
c = float(input("Informe o comprimento do lado c: "))

#q3#
# Verificar se os lados formam um triângulo válido
if a + b > c and a + c > b and b + c > a:
    # Verificar se o triângulo é retângulo usando o teorema de Pitágoras
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("O triângulo é retângulo!")
    else:
        print("O triângulo não é retângulo.")
else:
    print("Os lados não formam um triângulo válido.")



# Entrada do peso e altura
peso = float(input("Informe o peso (em kg): "))
altura = float(input("Informe a altura (em m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Avaliação do IMC
if imc < 18.5:
    avaliacao = "Magreza"
elif imc < 25:
    avaliacao = "Normal"
elif imc < 30:
    avaliacao = "Sobrepeso"
elif imc < 35:
    avaliacao = "Obesidade grau I"
elif imc < 40:
    avaliacao = "Obesidade grau II"
else:
    avaliacao = "Obesidade grau III"

# Exibição do resultado
print(f"IMC: {imc:.2f}")
print(f"Avaliação: {avaliacao}")


execucao = True

while execucao:
    print("Escolha uma opção:")
    print("1 - Cálculo do triângulo equilátero")
    print("2 - Cálculo do triângulo retângulo")
    print("3 - Cálculo do IMC")
    print("4 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        # Código para calcular triângulo equilátero
        a = float(input("Informe o comprimento do lado A: "))
        b = float(input("Informe o comprimento do lado B: "))
        c = float(input("Informe o comprimento do lado C: "))

        if a == b == c:
            print("O triângulo é equilátero!")
        else:
            print("O triângulo não é equilátero.")

    elif escolha == "2":
        # Código para calcular triângulo retângulo
        a = float(input("Informe o comprimento do lado a: "))
        b = float(input("Informe o comprimento do lado b: "))
        c = float(input("Informe o comprimento do lado c: "))

        if a + b > c and a + c > b and b + c > a:
            if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
                print("O triângulo é retângulo!")
            else:
                print("O triângulo não é retângulo.")
        else:
            print("Os lados não formam um triângulo válido.")

    elif escolha == "3":
        # Código para calcular IMC
        peso = float(input("Informe o peso (em kg): "))
        altura = float(input("Informe a altura (em m): "))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            avaliacao = "Magreza"
        elif imc < 25:
            avaliacao = "Normal"
        elif imc < 30:
            avaliacao = "Sobrepeso"
        elif imc < 35:
            avaliacao = "Obesidade grau I"
        elif imc < 40:
            avaliacao = "Obesidade grau II"
        else:
            avaliacao = "Obesidade grau III"

        print(f"IMC: {imc:.2f}")
        print(f"Avaliação: {avaliacao}")

    elif escolha == "4":
        print("Obrigado por usar nosso programa.")
        execucao = False

    else:
        print("Opção inválida. Tente novamente.")

    if escolha != "4":
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
        if opcao == 'N':
            execucao = False
            print("Obrigado por usar nosso programa.")