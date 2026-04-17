import pytest

@pytest.fixture
def lista_alunos_exemplo():
    return [
        {'nome': 'Ana', 'media': 8},
        {'nome': 'Bruno', 'media': 6},
        {'nome': 'Carlos', 'media': 10},]

@pytest.fixture
def lista_vazia():
    return []


@pytest.fixture
def lista_alunos_mista():
    return [
        {'nome': 'Ana', 'media': 8},   # aprovado
        {'nome': 'Bruno', 'media': 6}, # reprovado
        {'nome': 'Carlos', 'media': 7},# aprovado
        {'nome': 'Davi', 'media': 5},  # reprovado
    ]
