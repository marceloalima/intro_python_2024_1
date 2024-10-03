produtos1 = [['Iphone 12', 799, 'Eltronicos, Celulares'], ]

produtos2 = [('Iphone 12', 799, 'Eltronicos, Celulares'),]

produtos3 = [('Iphone 12', 799, ('Eletrônicos', 'Celulares'))]
print(produtos3[0][0]) # Iphone 12 
print(produtos3[0][2][0]) # Eletrônicos

produtos4 = [
    {'nome': 'Iphone 12', 'preco': 799, 'categorias': ('Eletrônicos', 'Celulares')},
    {'nome': 'Smart TV 55', 'preco': 2999.90, 'categorias': ('Eletrônicos', 'Televisores')},
    {'nome': 'Tenis nike', 'preco': 350.0, 'categorias': ('Moda', 'Calçados')}
]
print(produtos4[1]['categorias']) # ('Eletrônicos', 'Televisores')

