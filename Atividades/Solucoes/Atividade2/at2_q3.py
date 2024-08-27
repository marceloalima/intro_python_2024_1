nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media_aritmetica = (nota1 + nota2) / 2

if media_aritmetica >= 7 and media_aritmetica <= 10:
    print("Aprovado")
elif media_aritmetica < 4:
    print("Reprovado")
elif media_aritmetica >= 4 and media_aritmetica < 7:
    print("AF")
else:
    print("Resultado indefinido")