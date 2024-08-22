# Q.01 => Algoritmo que retorne o valor absoluto de um número

def valor_absoluto(numero):
    return abs(numero)
numero = -18
print("O valor absoluto de", numero, "é", valor_absoluto(numero))

# Q.02 => Faça um algorritmo que receba dois números e retorne o valor maior

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O maior número é {n1}')

# Q.03
'''Faça um algoritmo para calcular a média aritmética M entre duas notas de um aluno e mostrar sua situação, que pode ser: 
aprovado (M ≥ 7), 
reprovado (M < 4) e 
AF (4 ≤ M < 7). 
Se o aluno ficar de AF, entre com a nota da AF e mostre a média e o resultado final.'''

n1 = 10
n2 = 9
m = (n1 + n2) / 2
if m >= 7:
    print(f'Aprovado com média {m}')
else:
    if m < 4:
        print(f'Reprovado com média {m}')
    else:
        print('AF')
        af = float(input('Digite a nota da AF: '))
        m = (m + af) / 2
        if m >= 4:
            print(f'Aprovado com média {m}')
        else:
            print(f'Reprovado com média {m}')