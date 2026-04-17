from datetime import datetime



def data_cadastro():
    data = datetime.now()
    return data.strftime("%d/%m/%Y")

def adicionar_aluno(nome, nascimento, idade, nota1, nota2, media, aprovacao, cadastro, lista_alunos):
    alunos = {'nome' : nome, 'nascimento' : nascimento, 'idade'  : idade, 'nota1' : nota1,
              'nota2' : nota2, 'media' : media, 'aprovacao' : aprovacao, 'cadastro' : cadastro}
    lista_alunos.append(alunos)



def media_funcao(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media