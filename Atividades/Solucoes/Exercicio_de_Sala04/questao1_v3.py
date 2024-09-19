disciplinas = [[8, 7, 9, 10], [6], [10, 9, 8]]

medias = []

for disciplina in disciplinas:
    soma_notas = 0
    for nota in disciplina:
        soma_notas += nota

    media =  soma_notas / len(disciplina)
    medias.append(media)

print(medias)