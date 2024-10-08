''' 1.Crie um programa que recebe uma palavra ou frase.
2.Verifique se o conteudo digitado é um palíndromo.
Ex: Ala, Ele, Radar,...
Obs : Use SLICE da string'''

palavra = input("Digite uma frase ou palavra: ").upper().strip()
print(palavra)

palavra_reversa = ''.join(reversed(palavra))
print(palavra_reversa)

if palavra == palavra[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

''' quando usada a frase palíndromo:
"socorram me subi no onibus em marrocos"
    diz que a frase NÃO é um palindromo ;-; '''