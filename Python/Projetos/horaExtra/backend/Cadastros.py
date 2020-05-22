import pandas as pd

localFunc = r'.\Projetos\horaExtra\arquivos\funcionarios.csv'

def cadFunc(info):
    '''
    Função que cadastra funcionario no banco de dados funcionario.csv
    recebe uma lista com 3 dados: nome, cpf, cargo, salario e horas
    '''
    arquivo = open(localFunc, 'at')
    for p, i in enumerate(info):
        if p == len(info)-1:
            arquivo.write(f'{i}\n')
        else:
            arquivo.write(f'{i};')
    arquivo.close()

def dadosFunc(nome):
    '''
    Função responsável por encontrar o funcionario e retornar os dados dele
    '''
    arquivo = pd.read_csv(localFunc, delimiter=';')
    dado = arquivo.to_dict()
    for pos, func in dado['Nome'].items():
        if func == nome:
            return dado['Nome'][pos], str(dado['CPF'][pos]), dado['Cargo'][pos], dado['Salario'][pos], dado['Horas'][pos]
    return -1