from datetime import datetime, timedelta

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
    if nota < 7:
        aprovado = "Reprovado!"
        return aprovado
    else:
        aprovado = "Aprovado!"
        return aprovado

def adicionar_aluno(nome, nascimento, idade,  nota, aprovacao, cadastro, lista_alunos):
    alunos = {'nome' : nome, 'nascimento' : nascimento, 'idade'  : idade,
              'nota' : nota, 'aprovacao' : aprovacao, 'cadastro' : cadastro}
    lista_alunos.append(alunos)
    
def buscar_aluno(nome, lista_alunos):
    for alunos in lista_alunos:
        if alunos['nome'] == nome:
            return(f"\nNome: {alunos['nome']}\n"
                f"Idade: {alunos['idade']}\n"
                f"Data de nascimento: {alunos['nascimento']}\n"
                f"Nota: {alunos['nota']}\n"
                f"Situação: {alunos['aprovacao']}\n"
                f"Data do cadastro: {alunos['cadastro']}")
    
    return("\nNão encontrado\n")
            
def excluir_aluno(nome, lista_alunos):
    for alunos in lista_alunos:
        if alunos['nome'] == nome:
            lista_alunos.remove(alunos)
            return("\nAluno removido!\n")
    return("\nNão encontrado")

def lista_vazia(lista_alunos):
    if not lista_alunos:
        return False
    else:
        return True
    

def media_notas(lista_alunos):
    return sum(alunos['nota'] for alunos in lista_alunos) / len(lista_alunos)

def validar_nota(nota):
    if 0 > nota > 10:
        return False
    else:
        return True
    
def mensagem_nota():
    if not validar_nota(nota):
        print("A nota deve ser um valor de 0 a 10!")
        return False
    else:
        return True

    
    
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

