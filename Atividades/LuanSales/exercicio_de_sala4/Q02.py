produtos = []

produto1 = {
    'nome': 'Iphone 12',
    'preco': 3000,
    'categoria': 'Eletrônicos, Celulares'
}
produtos.append(produto1)
produto2 = {
    'nome': 'Smart TV 55',
    'preco': 2999.90,
    'categoria': 'Eletrônicos,Televisores'
}
produtos.append(produto2)
produto3 = {
    'nome': 'Tênis Nike',
    'preco': 350.00,
    'categoria': 'Moda, Calçados'
}
produtos.append(produto3)

for produto in produtos:
    print(f'Nome: {produto['nome']}')
    print(f'Preço: R$ {produto['preco']}')
    print(f'Categoria: {produto['categoria']}')
    print(' ')
