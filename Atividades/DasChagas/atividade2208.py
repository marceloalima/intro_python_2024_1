#primeira parte do exercício
num = int(input('DIGITE UM NÚMERO:'))
if num < 0:
    abs = num * (-1)
    print('O valor absoluto do seu número é: {}'.format(abs))
else:
    print ('O valor absoluto do seu número é {}'.format(num))

#segunda parte do exercício
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
if num1 > num2:
    print('O número {} é maior que {}!'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que {}!'.format(num2, num1))
else:
    print('os valores são iguais!!')

#TERCEIRA PARTE DO EXERCÍCIO
nota1 = float(input('DIGITE SUA PRIMEIRA NOTA:'))
nota2 = float(input('DIGITE A SEGUNDA NOTA:'))
media = (nota1 + nota2) / 2
if media >= 7:
    print('VOCÊ FOI APROVADO!')
elif media >= 4 and media < 7 :
    print('VOCÊ ESTÁ DE AF!')
    notaaf = float(input('DIGITE A SUA NOTA DA AF:'))
    media2 = (nota1 + nota2 + notaaf) / 3
    print ('Com a sua AF, sua média ficou igual {}!'.format(media2))
    if media2 >=7:
        print ('Parabéns, você foi aprovado!')
    else:
        print('Você foi reprovado! :( ')
else:
    print('VOCÊ ESTÁ REPROVADO!')