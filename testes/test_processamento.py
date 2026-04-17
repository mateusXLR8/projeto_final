from sistema.processamento import media_funcao, adicionar_aluno

def test_media_funcao():
    assert media_funcao(10, 10) == 10
    assert media_funcao(5, 7) == 6
    assert media_funcao(0, 10) == 5

def test_adicionar_aluno():
    lista = []

    adicionar_aluno(
        "Mateus",
        "01/01/2010",
        15,
        8,
        9,
        8.5,
        "Aprovado",
        "01/01/2024",
        lista
    )

    assert len(lista) == 1
    assert lista[0]['nome'] == "Mateus"
    assert lista[0]['media'] == 8.5
