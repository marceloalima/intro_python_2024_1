altura = float(input("Entre com sua altura em metros: "))
peso = float(input("Entre com seu peso em kg: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidade Grau I")
elif imc >= 35 and imc < 40:
    print("Obesidade Grau II")
elif imc >= 40:
    print("Obesidade Grau III")
else:
    print("Calculo errado.")
