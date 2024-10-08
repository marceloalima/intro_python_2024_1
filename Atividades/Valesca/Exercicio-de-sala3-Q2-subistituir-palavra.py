frase = input('Digite uma frase: ')
frase_velha = input('Qual a palavra da frase você quer mudar? : ')
frase_nova = input('Agora, digite a nova palavra: ')

frase_nova = frase.replace(frase_velha, frase_nova)
print(f'A nova frase é: {frase_nova}')