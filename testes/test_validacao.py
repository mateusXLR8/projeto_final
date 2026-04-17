from sistema.validacao import validar_nome, validar_nota, lista_vazia

def test_validar_nome():
    assert validar_nome("Mateus") == True
    assert validar_nome("Ana Clara") == True
    assert validar_nome("") == False
    assert validar_nome("Mateus123") == False

def test_validar_nota():
    assert validar_nota(0) == True
    assert validar_nota(10) == True
    assert validar_nota(5.5) == True
    assert validar_nota(-1) == False
    assert validar_nota(11) == False

def test_lista_vazia():
    assert lista_vazia([]) == False
    assert lista_vazia([1, 2, 3]) == True
