from sistema.funcoes import *

lista_alunos = []

while True:
    try:
        menu = int(input("""\nColoque o número referente a ação: 
    1 - Adicionar aluno
    2 - Listar alunos
    3 - Mostrar estatisticas
    4 - Gerar relatórios Excel
    5 - Sair\n \n
                    """))
        
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
                if nome.replace(" ","").isalpha(): 
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

            while True:
                try:
                    nota1 = float(input("\nDigite a primeira nota: ")) 
                    nota2 = float(input("Digite a segunda nota: "))
                except ValueError:
                    print("Digite apenas números.")
                    continue

                if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10 )  :
                    print("A nota não pode ser maior que 10 ou negativa")
                    continue
                media = (nota1 + nota2) / 2
                break

            aprovacao = aprovar(media)
            cadastro = data_cadastro()
            adicionar_aluno(nome,nascimento,idade,media,aprovacao,cadastro,lista_alunos)
            print(f'\n Aluno {nome} cadastrado com sucesso!')


        case 2:
            if lista_vazia(lista_alunos):
                print('\n =====LISTA DOS ALUNOS======')
                for i,aluno in enumerate(lista_alunos,start = 1):
                    print(f"\nAluno {i}")
                    print(f"Nome: {aluno['nome']}")
                    print(f"Idade: {aluno['idade']}")
                    print(f"Nascimento: {aluno['nascimento']}")
                    print(f"Nota: {aluno['nota']}")
                    print(f"Situação: {aluno['aprovacao']}")
                    print(f"Cadastro: {aluno['cadastro']}") 
            else:
                print("Nenhum aluno cadastrado")

        case 3:
            if lista_vazia(lista_alunos):
                print(f'\nMédia da turma:{media_notas(lista_alunos):.2f}')

                melhor = melhor_aluno(lista_alunos)
                print(f"\nMelhor aluno: {melhor['nome']} ({melhor['nota']})")
                aprovados,reprovados = separar_aluno(lista_alunos)
                print(f"\nAprovados:{aprovados}")
                print(f"\nReprovados {reprovados}")

            else:
                print('Nenhum aluno(a) consta como cadastrado.')
              
        case 4:
            print('Função Excel ainda não consta.')
        case 5:
            print("\nFechando programa...\n")
            break
        case _:
            print("\nNúmero invalido")
            continue
