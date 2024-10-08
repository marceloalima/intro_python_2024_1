disciplinas = [[8, 7, 9], [6, 5, 7], [10, 9, 8]]

medias = []

for disciplina in disciplinas:
    nota1 = disciplina[0]
    nota2 = disciplina[1]
    nota3 = disciplina[2]

    media = (nota1 + nota2 + nota3) / 3
    medias.append(media)

print(medias)