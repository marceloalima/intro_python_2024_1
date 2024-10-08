# Notas obtidas po um aluno
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# Média dos exercicios
media_exercicios = float(input('Digite a média dos exercícios: '))
media_de_aproveitamento = int(nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

if media_de_aproveitamento >= 9.0:
    conceito = 'A'
    print('Média de aproveitamento: ', media_de_aproveitamento)
    print('Conceito: ', conceito)
elif media_de_aproveitamento >= 7.5 < 9.0:
    conceito = 'B'
    print('Média de aproveitamento: ', media_de_aproveitamento)
    print('Conceito: ', conceito)
elif media_de_aproveitamento >= 6.0 < 7.5:
        conceito = 'C'
        print('Média de aproveitamento: ', media_de_aproveitamento)
        print('Conceito: ', conceito)
elif media_de_aproveitamento < 6.0:
            conceito = 'D'
            print('Média de aproveitamento: ', media_de_aproveitamento)
            print('Conceito: ', conceito)
    