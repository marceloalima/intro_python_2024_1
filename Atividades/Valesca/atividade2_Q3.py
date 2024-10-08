# Questão 3

nota1 = float(input("Digite a primera nota:"))
nota2 = float(input("Digite a segunda nota:"))
media_aritimetica =  (nota1 + nota2) / 2

if media_aritimetica >= 7 and media_aritimetica <= 10:
    print("Aprovado")
elif media_aritimetica < 4:
    print("Reprovado")
elif media_aritimetica >=4 and media_aritimetica < 7:
    print("AF")
else:
    print("Resultado indefinido")   