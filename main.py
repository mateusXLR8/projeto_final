from sistema.funcoes import *

lista_alunos = []

while True:
    try:
        menu = int(input("""\nColoque o número referente a ação: 
    1 - Adicionar aluno
    2 - Listar todos os alunos
    3 - Buscar aluno pelo nome
    4 - Remover aluno
    5 - Mostrar média geral das notas
    6 - Sair\n \n"""))
    except ValueError:
        print("Isso não é um número!")
        continue
    match menu:
        case 1:
            while True:   
                nome = input("\nDigite o nome do aluno: ").title().strip()
                try:
                    int(nome)
                    print("Utilize apenas letras")
                    continue
                except ValueError:
                    if not nome:
                        print("O nome não pode estar vazio!")
                        continue
                    break
            while True:        
                nascimento = input("\nColoque a data de nascimento do aluno em formato dd/mm/aaaa: ")
                try:
                    idade = idade_funcao(nascimento)
                except ValueError:
                    print("A data de nascimento deve estar no formato dd/mm/aaaa")
                    continue
                break
            while True:
                try:
                    nota = float(input("\nColoque a nota do aluno: "))
                except ValueError:
                    print("A nota deve ser um número")
                    continue
                if nota > 10 or nota < 0:
                    print("A nota não pode ser maior que 10 ou negativa")
                    continue
                break


            aprovacao = aprovar(nota)
            cadastro = data_cadastro()
            adicionar_aluno(nome, nascimento, idade, nota, aprovacao, cadastro, lista_alunos)
            print("Aluno adicionado!")
        case 2:
            if lista_vazia(lista_alunos):
                for alunos in lista_alunos:
                    print(f"\nNome: {alunos['nome']}\n"
                        f"Idade: {alunos['idade']}\n"
                        f"Data de nascimento: {alunos['nascimento']}\n"
                        f"Nota: {alunos['nota']}\n"
                        f"Situação: {alunos['aprovacao']}\n"
                        f"Data do cadastro: {alunos['cadastro']}") 
            else:
                print("Nenhum aluno cadastrado")

        case 3:
            if lista_vazia(lista_alunos):
                nome = input("Digite o nome do aluno: ").title().strip()  
                print(buscar_aluno(nome, lista_alunos,))
                continue
            else:
                print("Nenhum aluno cadastrado")
        case 4:
            if lista_vazia(lista_alunos):
                nome = input("\nDigite o nome do aluno: ").title().strip() 
                print(excluir_aluno(nome, lista_alunos))
            else:
                print("Nenhum aluno cadastrado")
        case 5:
            if lista_vazia(lista_alunos):
                print(f"A média geral dos alunos é: {media_notas(lista_alunos)} pontos")
            else:
                print("Nenhum aluno cadastrado")
        case 6:
            print("\nFechando programa...\n")
            break
        case _:
            print("\nNúmero invalido")
            continue
  
            

 
                    

                
                
               
                    
            
            
    



