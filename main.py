from sistema.estatisticas import *
from sistema.organizacao import *
from sistema.processamento import *
from sistema.relatorio import *
from sistema.saida import *
from sistema.validacao import *

lista_alunos = []

while True:
    try:
        menu = int(input("""\nColoque o número referente a ação: 
    1 - Adicionar aluno
    2 - Listar alunos
    3 - Mostrar estatisticas
    4 - Gerar relatórios Excel
    0 - Sair\n
-------->  """))
        
    except ValueError:
        print("Isso não é um número!")
        continue

    match menu:
        case 1:
            while True:   
                nome = input("\nDigite o nome do aluno: ").title().strip()
                if not validar_nome(nome):
                    continue
                break
            while True:        
                try:
                    nascimento = input("\nColoque a data de nascimento do aluno em formato dd/mm/aaaa: ")
                    idade = idade_funcao(nascimento)
                except ValueError:
                    print("A data de nascimento deve estar no formato dd/mm/aaaa")
                    continue 

                if validar_idade(nascimento):
                    break
                else:
                    print('A idade deve ser maior que 12 e menor que 18')
                    continue         
            
            while True:
                try:
                    nota1 = float(input("\nDigite a primeira nota: ")) 
                    nota = nota1
                    if not validar_nota(nota):
                        print("A nota não pode ser maior que 10 ou negativa")
                        continue
                    else:
                        break
                except ValueError:
                    print("Digite apenas números.")
                    continue
            while True:  
                try:     
                    nota2 = float(input("Digite a segunda nota: "))
                    nota = nota2
                    if not validar_nota(nota):
                        print('A nota não pode ser maior que 10 ou negativa')
                        continue
                    else:
                        break
                except ValueError:
                    print("Digite apenas números")
                    continue        
 
            media = media_funcao(nota1, nota2)
            
            aprovacao = aprovar(media)
            cadastro = data_cadastro()
            adicionar_aluno(nome,nascimento,idade,nota1,nota2,media,aprovacao,cadastro,lista_alunos)
            print(f'\n Aluno {nome} cadastrado com sucesso!')


        case 2:
            listar_alunos(lista_alunos)

        case 3:
            estatistica(lista_alunos)
        case 4:
            if lista_vazia(lista_alunos):
                salvar_excel(lista_alunos)
                print("Alunos salvos")
            else:
                print("Nenhum aluno cadastrado")
        case 0:
            print("\nFechando programa...\n")
            break
        case _:
            print("\nNúmero invalido")
            continue
