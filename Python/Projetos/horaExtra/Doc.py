import pandas as pd
bancoDeDados = r'.\Projetos\horaExtra\arquivos\funcionarios.csv'
modelo = r'.\Projetos\horaExtra\arquivos\modelo.pdf'
def geraRecibo():
    arquivo = open(modelo, 'r')
    teste = arquivo.read()
    
def attHora(cpf, hora):
    dados = pd.read_csv(bancoDeDados, delimiter=';')
    posi = -1
    #percorre o data frame para encontrar o individuo
    for pos, valor in dados['CPF'].items():
        if valor == cpf:
            posi = pos
            break
    if posi == -1:
        return -1
    dados['Horas'][posi] += hora
    dados.to_csv(bancoDeDados, index=False, sep=';')
