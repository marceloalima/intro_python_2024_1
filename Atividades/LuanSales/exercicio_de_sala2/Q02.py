# Q. 02
'''
Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas. 
A saída do programa deve indicar se o triângulo é ou não um triângulo retângulo.
(teorema de pitágoras: quadrado de um dos lados deve ser a soma dos quadrados dos outros dois lados).
'''
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
teorema = (lado1 ** 2) + (lado2 ** 2) == (lado3 ** 2)
if teorema:
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")
print("Fim do programa.")

