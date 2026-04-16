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
                if not nome:
                    print("O nome não pode estar vazio!")
                    continue
                if nome.isalpha(): 
                    break
                else:
                    print("Utilize apenas letras")
                    
            while True:        

                try:
                    nascimento = input("\nColoque a data de nascimento do aluno em formato dd/mm/aaaa: ")
                    idade = idade_funcao(nascimento)
                except ValueError:
                    print("A data de nascimento deve estar no formato dd/mm/aaaa")
                    continue
        
                if calcular_idade(nascimento):
                    break
                else:
                    print('A idade deve ser maior que 12 e menor que 18')
                    continue
            
            
            try:
                while True:
                    nota1 = float(input("\nColoque a primeira nota do aluno: "))
                    nota = nota1
                    if not validar_nota(nota):
                        print("A nota deve estar entre 0 e 10")
                        continue
                    break
                    
                while True:
                    nota2 = float(input("\nColoque a segunda nota: "))
                    nota = nota2
                    if not validar_nota(nota):
                        print("A nota deve estar entre 0 e 10")
                        continue
                    break
                media = (nota1+nota2)/2
            except ValueError:
                print("A nota deve ser um número")
                continue
            


            aprovacao = aprovar(media)
            cadastro = data_cadastro()
            adicionar_aluno(nome, nascimento, idade, media, aprovacao, cadastro, lista_alunos)
            print("Aluno adicionado!")
        case 2:
            listar_alunos(lista_alunos)

        case 3:
            nome = input("Digite o nome do aluno: ").title().strip()  
            buscar_aluno(lista_alunos, nome)

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
