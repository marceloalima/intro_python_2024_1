# Dados de entradas
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo (M/F): ')
# Cálculo do peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f}')
if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f}')
