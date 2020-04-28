import csv
import os
arquivo = open(os.path.join(os.path.dirname(__file__), 'teste.csv'))

# linhas = csv.reader(arquivo)
# lista = []

# print("=-"*30)
# for linha in linhas: #forma de percorrer todo array
#     lista.append(linha) #criando uma lista
# print("=-"*30)
# print(lista)

pessoas = csv.DictReader(arquivo)
galera = dict()
pessoal = list()
for pessoa in pessoas:
    galera['nome'] = pessoa['nome']
    galera['idade'] = pessoa['idade']
    galera['email'] = pessoa['email']
    pessoal.append(galera.copy())
    galera.clear()
for p in pessoal:
    print(p['nome'])