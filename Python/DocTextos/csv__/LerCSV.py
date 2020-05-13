

# linhas = csv.reader(arquivo)
# lista = []

# print("=-"*30)
# for linha in linhas: #forma de percorrer todo array
#     lista.append(linha) #criando uma lista
# print("=-"*30)
# print(lista)
import csv
arquivo = open('DocTextos/csv__/teste.csv', 'r') #arquivo de origem
file = open('DocTextos/csv__/ml.csv', 'w') #arquivo destino

pessoas = csv.DictReader(arquivo)
pessoal = list()
for pessoa in pessoas:
    info = list()
    for key, atrib in pessoa.items():#para cada linha, eu extraio as informações sem as keys
        info.append(atrib)
    pessoal.append(info[:])
    info.clear()

write = csv.writer(file, delimiter=',', lineterminator='\n')
write.writerows((pessoal[i] for i in range(len(pessoal))))