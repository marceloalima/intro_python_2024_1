turmas_1 = [
    {'turma': 'A', 'professor': 'João', 'alunos': [('Ana', 14), ('Carlos', 15), ('Beatriz', 13)], 'materias': ('Matemática', 'Ciências', 'Historia')},
    {'turma': 'B', 'professor': 'Maria', 'alunos': [('Pedro', 16), ('Carlos', 15), ('Beatriz', 13)], 'materias': ('Matemática', 'Ciências', 'Historia')}
]

print(turmas_1[0]['professor'])
print(turmas_1[0]['alunos'])

turmas_2 = {
    "Turma A": {'prof': 'Joao', 'alunos': [('Ana', 14), ('Carlos', 15), ('Beatriz', 13)], 'materias': ('Matemática', 'Ciências', 'Historia')},
    "Turma B": {'prof': 'Maria', 'alunos': [('Pedro', 16), ('Lucas', 14), ('Paula', 15)], 'materias': ('Geografia', 'Matemática', 'Inglês')},
}

print(turmas_2["Turma A"]['prof'])