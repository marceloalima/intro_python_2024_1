# Notas dos alunos em Matemática, Física e Português ao longo de 3 avaliações
notas = notas = {
    'João': {'Matematica': [8, 7, 9], 'Fisica': [6, 7, 0], 'Portugues': [9, 8, 7]},
    'Maria': {'Matematica': [7, 6, 8], 'Fisica': [5, 6, 0], 'Portugues': [10, 9, 8]},
    'Carlos': {'Matematica': [6, 5, 7], 'Fisica': [7, 6, 8], 'Portugues': [8, 9, 7]},
    'Ana': {'Matematica': [9, 8, 7], 'Fisica': [7, 6, 9], 'Portugues': [10, 9, 8]},
    'Pedro': {'Matematica': [5, 6, 7], 'Fisica': [7, 8, 6], 'Portugues': [9, 8, 7]},
    'Luiza': {'Matematica': [6, 8, 9], 'Fisica': [6, 5, 0], 'Portugues': [10, 9, 8]},
    'Paulo': {'Matematica': [7, 8, 9], 'Fisica': [7, 6, 8], 'Portugues': [8, 7, 9]},
    'Fernanda': {'Matematica': [8, 7, 6], 'Fisica': [8, 7, 6], 'Portugues': [10, 9, 8]},
    'Bruno': {'Matematica': [6, 7, 6], 'Fisica': [6, 5, 7], 'Portugues': [8, 9, 7]},
    'Carla': {'Matematica': [9, 8, 7], 'Fisica': [8, 9, 8], 'Portugues': [9, 9, 8]},
    'Rafael': {'Matematica': [7, 6, 7], 'Fisica': [6, 5, 7], 'Portugues': [7, 6, 8]},
    'Gabriela': {'Matematica': [8, 9, 8], 'Fisica': [7, 6, 9], 'Portugues': [9, 10, 9]},
    'Marcos': {'Matematica': [6, 5, 6], 'Fisica': [7, 8, 6], 'Portugues': [8, 9, 7]},
    'Juliana': {'Matematica': [9, 8, 9], 'Fisica': [7, 6, 7], 'Portugues': [9, 8, 9]},
    'Rodrigo': {'Matematica': [6, 7, 8], 'Fisica': [6, 7, 5], 'Portugues': [9, 8, 7]},
    'Daniela': {'Matematica': [9, 7, 8], 'Fisica': [6, 5, 6], 'Portugues': [10, 9, 8]},
    'Thiago': {'Matematica': [8, 7, 9], 'Fisica': [8, 9, 7], 'Portugues': [9, 10, 9]},
    'Lucas': {'Matematica': [7, 6, 8], 'Fisica': [7, 6, 8], 'Portugues': [8, 9, 8]},
    'Larissa': {'Matematica': [9, 8, 9], 'Fisica': [7, 6, 8], 'Portugues': [10, 9, 9]},
    'Felipe': {'Matematica': [7, 6, 7], 'Fisica': [6, 7, 5], 'Portugues': [8, 7, 7]},
}
    
# Função para calcular a média das três notas
def calcular_media(notas_disciplina):
    return sum(notas_disciplina) / len(notas_disciplina)

# Processar dados de cada aluno
for aluno, disciplinas in notas.items():
    medias = {}
    
    # Calcula a média de cada disciplina
    for disciplina, notas_disciplina in disciplinas.items():
        media = calcular_media(notas_disciplina)
        medias[disciplina] = media
        print(f'{aluno} - Média em {disciplina}: {media:.2f}')
    
    # Identifica melhor e pior desempenho
    melhor_disciplina = max(medias, key=medias.get)
    pior_disciplina = min(medias, key=medias.get)
    
    print(f'{aluno} - Melhor desempenho: {melhor_disciplina} com média {medias[melhor_disciplina]:.2f}')
    print(f'{aluno} - Pior desempenho: {pior_disciplina} com média {medias[pior_disciplina]:.2f}')
    print('-' * 40)

