

def separar_aluno(lista_alunos):
    aprovados = 0
    reprovados = 0
    for aluno in lista_alunos:
        if aluno['media'] >= 7: 
            aprovados += 1 
        else:
            reprovados += 1 

    return aprovados, reprovados