palavra = input('Digite uma palavra: ')
palavra = palavra.lower()
palavra = palavra.replace(' ', '')
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print(f'A palavra {palavra_invertida} é um palíndromo')
else:
    print(f'A palavra {palavra_invertida} não é um palíndromo')
    print(' ')
    print("Fim do programa")
 



