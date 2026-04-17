from sistema.estatisticas import media_notas, melhor_aluno

def test_media_notas(lista_alunos_exemplo):
    assert media_notas(lista_alunos_exemplo) == 8

def test_melhor_aluno(lista_alunos_exemplo):
    melhor = melhor_aluno(lista_alunos_exemplo)

    assert melhor['nome'] == 'Carlos'
    assert melhor['media'] == 10

from sistema.validacao import lista_vazia as func_lista_vazia

def test_lista_vazia(lista_vazia):
    assert func_lista_vazia(lista_vazia) == False
