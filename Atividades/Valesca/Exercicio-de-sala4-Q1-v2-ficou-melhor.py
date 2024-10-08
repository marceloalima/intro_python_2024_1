aluno = [[8,7,9],[6,5,7],[10,9,8]]
matematica = aluno[0]
quimica = aluno[1]
fisica = aluno[2]
print(matematica,quimica,fisica)

# matematica
soma_de_matematica = 0

for nota in matematica:
    soma_de_matematica += nota


media_de_matematica = soma_de_matematica / len(matematica)
print(media_de_matematica)

# quimica
soma_de_quimica = 0

for nota in quimica:
    soma_de_quimica += nota


media_de_quimica = soma_de_quimica / len(quimica)
print(media_de_quimica)

# fisica
soma_de_fisica = 0

for nota in fisica:
    soma_de_fisica += nota


media_de_fisica = soma_de_fisica / len(fisica)
print(media_de_fisica)

'''essa versao eu consegui fazer melhor com o "for"
    depois da explicação do prof.
     ainda tive uma dificuldadezinha ;-; '''