media = []
notas = {
    "Matemática": [8, 7, 9],
    "Física": [6, 5, 7],
    "Química": [10, 9, 8]
}
for materia, notas_materia in notas.items():
    media_materia = sum(notas_materia) / len(notas_materia)
    media.append(media_materia)
    print(f"Média de {materia}: {media_materia}")
print(media)


