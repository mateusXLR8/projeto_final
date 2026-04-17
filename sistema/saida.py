
from sistema.estatisticas import *
from sistema.organizacao import *
from sistema.processamento import *
from sistema.relatorio import *
from sistema.validacao import *



    

    
def aprovar(nota):
    return "Aprovado!" if nota >= 7 else "Reprovado!"
              

                        
def exibir_aluno(aluno):
    print(f"\nNome: {aluno['nome']}\n"
          f"Idade: {aluno['idade']}\n"
          f"Média: {aluno['media']}\n"
          f"Situação: {aluno['aprovacao']}\n")
        

             
    
def listar_alunos(lista_alunos):
    if not lista_vazia(lista_alunos):
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in lista_alunos:
        exibir_aluno(aluno)
            

    



    
    






    