from sistema.organizacao import separar_aluno

def test_separar_aluno(lista_alunos_mista):
    aprovados, reprovados = separar_aluno(lista_alunos_mista)

    assert aprovados == 2
    assert reprovados == 2


def test_todos_aprovados():
    alunos = [
        {'nome': 'A', 'media': 7},
        {'nome': 'B', 'media': 9},
    ]

    aprovados, reprovados = separar_aluno(alunos)

    assert aprovados == 2
    assert reprovados == 0

def test_todos_reprovados():
    alunos = [
        {'nome': 'A', 'media': 5},
        {'nome': 'B', 'media': 6},
    ]

    aprovados, reprovados = separar_aluno(alunos)

    assert aprovados == 0
    assert reprovados == 2
