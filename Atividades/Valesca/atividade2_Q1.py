# Exercicio de sala 2 - Questão 1

'''
Escreva um programa que aceite os comprimentos de três lados de um triângulo como entradas.
A saída do programa deve indicar se o triângulo é ou não um triângulo equilátero.

'''

numero = int(input('Digite um número: '))

if numero < 0:
    numero = numero * -1

print('O valor absoluto é:',numero)