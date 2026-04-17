
from sistema.organizacao import *
from sistema.processamento import *
from sistema.relatorio import *
from sistema.validacao import *

def media_notas(lista_alunos):
    return sum(aluno['media'] for aluno in lista_alunos) / len(lista_alunos)

def melhor_aluno(lista_alunos):
    melhor = lista_alunos[0]
    for aluno in lista_alunos:
        if aluno['media'] > melhor['media']:
            melhor = aluno
    return melhor

def estatistica(lista_alunos):
        if lista_vazia(lista_alunos):   
            print(f'\nMédia da turma:{media_notas(lista_alunos):.2f}')
            melhor = melhor_aluno(lista_alunos)
            print(f"\nMelhor aluno: {melhor['nome']} ({melhor['media']})")
            aprovados,reprovados = separar_aluno(lista_alunos)
            print(f"\nAprovados:{aprovados}")
            print(f"\nReprovados {reprovados}")
        else:
            print("Nenhum aluno cadastrado")