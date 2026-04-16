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
    return "Aprovado!" if nota >= 7 else "Reprovado!"

def adicionar_aluno(nome, nascimento, idade,  nota, aprovacao, cadastro, lista_alunos):
    aluno = {
            'nome': nome,
            'nascimento': nascimento,
            'idade': idade,
            'nota': nota,
            'aprovacao': aprovacao, 
            'cadastro': cadastro
            }
    
    lista_alunos.append(aluno)   

def listar_alunos(lista_alunos):
    for alunos in lista_alunos:
            print(f"\nNome: {alunos['nome']}\n"
                f"Idade: {alunos['idade']}\n"
                f"Data de nascimento: {alunos['nascimento']}\n"
                f"Nota: {alunos['nota']}\n"
                f"Situação: {alunos['aprovacao']}\n"
                f"Data do cadastro: {alunos['cadastro']}")
            
def lista_vazia(lista_alunos):
    if not lista_alunos:
        return False
    else:
        return True
    
def media_notas(lista_alunos):
    return sum(alunos['nota'] for alunos in lista_alunos) / len(lista_alunos)

def melhor_aluno(lista_alunos):
    melhor = lista_alunos[0]

    for aluno in lista_alunos:
        if aluno['nota'] > melhor['nota']:
            melhor = aluno
    return melhor

def separar_aluno(lista_alunos):
    aprovados = 0
    reprovados = 0

    for aluno in lista_alunos:
        if aluno['nota'] >= 7: 
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