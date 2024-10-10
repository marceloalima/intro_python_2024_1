def calcular_media(notas):
    return sum(notas) / len(notas)

def melhor_pior_disciplinas(medias):
    melhores = {}
    piores = {}
    for aluno, disciplinas in medias.items():
        melhores[aluno] = max(disciplinas, key=disciplinas.get)
        piores[aluno] = min(disciplinas, key=disciplinas.get)
    return melhores, piores

def main():
    with open('primeiro_ano.txt', 'r') as file:
        linhas = file.readlines()

    medias = {}

    for linha in linhas:
        # Processa cada linha para extrair as informações
        dados = linha.strip().split(' -> ')
        nome = dados[0]
        
        notas_matematica = list(map(float, dados[1].split(': ')[1].split(', ')))
        notas_fisica = list(map(float, dados[2].split(': ')[1].split(', ')))
        notas_portugues = list(map(float, dados[3].split(': ')[1].split(',')))

        media_matematica = calcular_media(notas_matematica)
        media_fisica = calcular_media(notas_fisica)
        media_portugues = calcular_media(notas_portugues)

        medias[nome] = {
            'Matemática': media_matematica,
            'Física': media_fisica,
            'Português': media_portugues
        }

    # Identifica as melhores e piores disciplinas
    melhores, piores = melhor_pior_disciplinas(medias)

    # Exibe os resultados
    for aluno, disciplinas in medias.items():
        print(f"{aluno}:")
        print(f"  Médias: {disciplinas}")
        print(f"  Melhor desempenho em: {melhores[aluno]}")
        print(f"  Pior desempenho em: {piores[aluno]}\n")

if __name__ == "__main__":
    main()
