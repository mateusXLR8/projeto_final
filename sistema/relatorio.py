from openpyxl import Workbook



def salvar_excel(lista_alunos):
    aprovados = Workbook()
    reprovados = Workbook()
    planilha_reprovados = reprovados.active
    planilha_aprovados = aprovados.active
    planilha_aprovados.title = 'ALUNOS'
    planilha_reprovados.title = 'ALUNOS'
    planilha_aprovados.append(['NOME', 'NOTA 1', 'NOTA 2', 'MÉDIA', 'STATUS'])
    planilha_reprovados.append(['NOME', 'NOTA 1', 'NOTA 2', 'MÉDIA', 'STATUS'])
    for alunos in lista_alunos:
        celulas = ([alunos['nome'], alunos['nota1'], alunos['nota2'], alunos['media'], alunos['aprovacao']])
        if alunos['media'] >= 7:
            planilha_aprovados.append(celulas)
        else:
            planilha_reprovados.append(celulas)
    aprovados.save('APROVADOS.xlsx')
    reprovados.save('REPROVADOS.xlsx')