from datetime import datetime



def validar_nome(nome):
    if not nome:
        print("O nome não pode estar vazio")
        return False            
    if nome.replace(" ", "").isalpha():
        return True
    else:
        print("Utilize apenas letras")
        return False
    
def idade_funcao(nascimento):
    agora = datetime.now()
    nascimento_convertida = datetime.strptime(nascimento, "%d/%m/%Y")
    idade_funcao = agora.year - nascimento_convertida.year
    if agora.month < nascimento_convertida.month:
        idade_funcao = idade_funcao - 1
        return idade_funcao 
    else:
        return idade_funcao
    
def validar_nota(nota):
    return 0 <= nota <= 10

def validar_idade(nascimento):
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

def lista_vazia(lista_alunos):
    if not lista_alunos:
        return False
    else:
        return True