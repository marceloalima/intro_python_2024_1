# Q. 01
'''
Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas. 
A saída do programa deve indicar se o triângulo é ou não um triângulo equilátero.
'''
lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")

print("Fim do programa.")