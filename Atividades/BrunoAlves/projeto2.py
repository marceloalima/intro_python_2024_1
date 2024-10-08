# Dicionário com as notas dos alunos
notas = {
    'João': {'Matemática': [8, 7, 9], 'Física': [6, 7, 0], 'Português': [9, 8, 7]},
    'Maria': {'Matemática': [7, 6, 8], 'Física': [5, 6, 0], 'Português': [10, 9, 8]},
    'Carlos': {'Matemática': [6, 5, 7], 'Física': [7, 6, 8], 'Português': [8, 9, 7]},
    'Ana': {'Matemática': [9, 8, 7], 'Física': [7, 6, 9], 'Português': [10, 9, 8]},
    'Pedro': {'Matemática': [5, 6, 7], 'Física': [7, 8, 6], 'Português': [9, 8, 7]},
    'Luiza': {'Matemática': [6, 8, 9], 'Física': [6, 5, 0], 'Português': [10, 9, 8]},
    'Paulo': {'Matemática': [7, 8, 9], 'Física': [7, 6, 8], 'Português': [8, 7, 9]},
    'Fernanda': {'Matemática': [8, 7, 6], 'Física': [8, 7, 6], 'Português': [10, 9, 8]},
    'Bruno': {'Matemática': [6, 7, 6], 'Física': [6, 5, 7], 'Português': [8, 9, 7]},
    'Carla': {'Matemática': [9, 8, 7], 'Física': [8, 9, 8], 'Português': [9, 9, 8]},
    'Rafael': {'Matemática': [7, 6, 7], 'Física': [6, 5, 7], 'Português': [7, 6, 8]},
    'Gabriela': {'Matemática': [8, 9, 8], 'Física': [7, 6, 9], 'Português': [9, 10, 9]},
    'Marcos': {'Matemática': [6, 5, 6], 'Física': [7, 8, 6], 'Português': [8, 9, 7]},
    'Juliana': {'Matemática': [7, 8, 9], 'Física': [6, 7, 8], 'Português': [9, 9, 8]}
}

# Função para calcular a média de cada aluno
def calcular_media(notas_aluno):
    medias = {}
    for disciplina, notas in notas_aluno.items():
        # Calcula a média das notas da disciplina
        media = sum(notas) / len(notas)
        medias[disciplina] = round(media, 2)  # Arredonda a média para duas casas decimais
    return medias

# Calcula a média de cada aluno
medias = {}
for aluno, notas_aluno in notas.items():
    medias[aluno] = calcular_media(notas_aluno)

# Imprime o resultado
for aluno, media_aluno in medias.items():
    print(f"Aluno: {aluno}")
    # Encontra a disciplina com a melhor e pior nota
    melhor_desempenho = max(media_aluno, key=media_aluno.get)
    pior_desempenho = min(media_aluno, key=media_aluno.get)
    print(f"Melhor desempenho: {melhor_desempenho} com média {media_aluno[melhor_desempenho]}")
    print(f"Pior desempenho: {pior_desempenho} com média {media_aluno[pior_desempenho]}")
    print()