#Faça um algoritmo que retorne o valor absoluto de um número.#
num = float(input("Digite um número: "))

if num < 0: num = num * -1

print("O valor absoluto do número é:", num)

#Faça um algoritmo que receba dois números e retorne o valor do maior.#
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2: 
    print("O maior número é:", num1)
else: print("O maior número é:", num2)

#Faça um algoritmo para calcular a média aritmética M entre duas notas de um aluno e mostrar sua situação, que pode ser

#aprovado, reprovado ou de recuperação. #

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2 
aprovado= ( media > 7)

af = (media >= 4 and media < 7)

if media > 7: 
    print("Situação: Aprovado")
elif media < 4: 
    print("Situação: Reprovado")
else: 
    print("Situação: af")
