# Questão 2
'''
Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas.
A saída do programa deve indicar se o triângulo é ou não um triângulo retângulo.
(teorema de pitágoras: quadrado de um dos lados deve ser a soma dos quadrados dos outros dois lados).

'''

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2 :
    print(n1," é o maior que",n2)

elif n2 > n1:
    print(n2," é o maior que",n1)

else:
    print(n1,"é igual a", n2)