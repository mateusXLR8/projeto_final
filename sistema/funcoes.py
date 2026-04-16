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

def adicionar_aluno(nome, nascimento, idade, media, aprovacao, cadastro, lista_alunos):
    alunos = {'nome' : nome, 'nascimento' : nascimento, 'idade'  : idade,
              'media' : media, 'aprovacao' : aprovacao, 'cadastro' : cadastro}
    lista_alunos.append(alunos)
                        
def exibir_aluno(aluno):
    print(f"\nNome: {aluno['nome']}\n"
          f"Idade: {aluno['idade']}\n"
          f"Data de nascimento: {aluno['nascimento']}\n"
          f"Média: {aluno['media']}\n"
          f"Situação: {aluno['aprovacao']}\n"
          f"Data do cadastro: {aluno['cadastro']}")
    
    
def buscar_aluno(lista_alunos, nome_busca):
    for aluno in lista_alunos:
        if aluno['nome'].title().strip()  == nome_busca.title().strip(): 
            exibir_aluno(aluno)
            return
    print("Aluno não encontrado.")



    
def listar_alunos(lista_alunos):
    if not lista_vazia(lista_alunos):
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in lista_alunos:
        exibir_aluno(aluno)
    
            
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
    return 0 <= nota <= 10
    
def mensagem_nota():
    return "A nota deve estar entre 0 e 10!"

    
    
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
    



