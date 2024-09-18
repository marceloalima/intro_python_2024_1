disciplinas = [[8, 7, 9], [6, 5, 7], [10, 9, 8]]
notas_de_matematica = disciplinas[0]
notas_de_fisica = disciplinas[1]
notas_de_quimica = disciplinas[2]

# Calculando a média de matemática
soma_notas_matematica = 0

for nota in notas_de_matematica:
    soma_notas_matematica += nota

media_de_matematica = soma_notas_matematica / len(notas_de_matematica)

# Calculando a média de física
soma_notas_fisica = 0
for nota in notas_de_fisica:
    soma_notas_fisica += nota

media_de_fisica = soma_notas_fisica / len(notas_de_fisica)

# Calculando a média de química
soma_notas_quimica = 0
for nota in notas_de_quimica:
    soma_notas_quimica += nota

media_de_quimica = soma_notas_quimica / len(notas_de_quimica)

# Saída
medias = [media_de_matematica, media_de_fisica, media_de_quimica]

print(medias)