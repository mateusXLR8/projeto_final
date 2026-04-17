from datetime import datetime, timedelta
from openpyxl import Workbook

def idade_funcao(nascimento):
    agora = datetime.now()
    nascimento_convertida = datetime.strptime(nascimento, "%d/%m/%Y")
    idade_funcao = agora.year - nascimento_convertida.year
    if agora.month < nascimento_convertida.month:
        idade_funcao = idade_funcao - 1
        return idade_funcao 
    else:
        return idade_funcao
    
def data_cadastro():
    data = datetime.now()
    return data.strftime("%d/%m/%Y")
    
def aprovar(nota):
    return "Aprovado!" if nota >= 7 else "Reprovado!"
              
def adicionar_aluno(nome, nascimento, idade, media, aprovacao, cadastro, lista_alunos):
    alunos = {'nome' : nome, 'nascimento' : nascimento, 'idade'  : idade,
              'media' : media, 'aprovacao' : aprovacao, 'cadastro' : cadastro}
    lista_alunos.append(alunos)
                        
def exibir_aluno(aluno):
    print(f"\nNome: {aluno['nome']}\n"
          f"Idade: {aluno['idade']}\n"
          f"Média: {aluno['media']}\n"
          f"Situação: {aluno['aprovacao']}\n")
        
def buscar_aluno(lista_alunos, nome_busca):
    for aluno in lista_alunos:
        if aluno['nome'].title().strip() == nome_busca.title().strip(): 
            exibir_aluno(aluno)
            return
    print("Aluno não encontrado.")
    
def listar_alunos(lista_alunos):
    if not lista_vazia(lista_alunos):
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in lista_alunos:
        exibir_aluno(aluno)
            
def lista_vazia(lista_alunos):
    if not lista_alunos:
        return False
    else:
        return True
    
def media_notas(lista_alunos):
    return sum(aluno['media'] for aluno in lista_alunos) / len(lista_alunos)


def melhor_aluno(lista_alunos):
    melhor = lista_alunos[0]
    for aluno in lista_alunos:
        if aluno['media'] > melhor['media']:
            melhor = aluno
    return melhor

def separar_aluno(lista_alunos):
    aprovados = 0
    reprovados = 0
    for aluno in lista_alunos:
        if aluno['media'] >= 7: 
            aprovados += 1 
        else:
            reprovados += 1 

    return aprovados, reprovados
    
    
def calcular_idade(nascimento):
    hoje = datetime.now() 
    nascimento_convertida = datetime.strptime(nascimento, "%d/%m/%Y") 
    
    if nascimento_convertida > hoje: 
        return False
    
    diferenca = hoje - nascimento_convertida 
    idade_calculo = diferenca.days // 365 
    
    if idade_calculo > 120: 
        return False
    elif idade_calculo < 12 or idade_calculo > 18: 
        return False
    else:
        return True 

def validar_nota(nota):
    return 0 <= nota <= 10

def salvar_excel(lista_alunos):
    arquivo = Workbook()
    planilha = arquivo.active
    planilha.title = 'ALUNOS'
    planilha.append(['NOME', 'NOTA 1', 'NOTA 2', 'MÉDIA', 'STATUS'])
    for alunos in lista_alunos:
        planilha.append([alunos['nome'], alunos['nota1'], alunos['nota2'], alunos['media'], alunos['aprovacao']])