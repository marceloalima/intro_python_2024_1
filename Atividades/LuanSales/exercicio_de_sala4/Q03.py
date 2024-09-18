turmas = []
turma_a = {
    "turma": "A",
    "professor": "João",
    "alunos": [("Ana", 14), ("Carlos", 15), ("Beatriz", 13)],
    "materias": ["Matemática", "Ciências", "História"]
}
turmas.append(turma_a)

turma_b = {
    "turma": "B",
    "professor": "Maria",
    "alunos": [("Pedro", 16), ("Lucas", 14), ("Paula", 15)],
    "materias": ["Geografia", "Matemática", "Inglês"]
}
turmas.append(turma_b)

turma_c = {
    "turma": "C",
    "professor": "José",
    "alunos": [("Fernanda", 17), ("Gabriel", 16), ("Luiza", 16)],
    "materias": ["Biologia", "Química", "Física"]
}
turmas.append(turma_c)

for turma in turmas:
    print("Turma", turma["turma"])
    print("Prof.:", turma["professor"])
    print("Alunos:")

    for aluno in turma["alunos"]:
        print(f'- {aluno[0]}, {(aluno[1])} anos de idade')
    print("Materias:", ", ".join(turma["materias"]))
    print("-" * 40)

print('FIM DO PROGRAMA')