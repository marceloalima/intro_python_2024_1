# Q. 03
'''
O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m), de acordo com a seguinte fórmula: IMC = peso / (altura x altura). 
A tabela abaixo apresenta como avaliar os resultados do IMC.
TABELA DE CLASSIFICAÇÃO DE IMC
Abaixo de 18,5 Abaixo do peso
Entre 18,5 e 25	Peso normal
Entre 25 e 30 Sobrepeso
Entre 30 e 35 Obesidade grau I
Entre 35 e 40 Obesidade grau II
Acima de 40	Obesidade grau III
Baseado nessas informações, crie um programa que recebe como entrada:
o nome da pessoa, peso em kg e altura em metros, e imprima na saída a classificação desse paciente.
'''
nome = input("Digite o seu nome: ")
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"{nome} está ABAIXO do peso.")
elif imc >= 18.5 and imc < 25:
    print(f"{nome} está com o peso NORMAL.")
elif imc >= 25 and imc < 30:
    print(f"{nome} está com SOBREPESO.")
elif imc >= 30 and imc < 35:
    print(f"{nome} está com OBESIDADE GRAU I.")
elif imc >= 35 and imc < 40:
    print(f"{nome} está com OBESIDADE GRAU II.")
elif imc >= 40:
    print(f"{nome} está com OBESIDADE GRAU III.")
print("Fim do programa.")
