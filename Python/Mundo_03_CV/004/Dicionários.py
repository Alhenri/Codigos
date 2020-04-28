dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
filme ={
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())#retorna todos os valores
print(filme.keys())#retorna os indices
print(filme.items())#retorna tudo
for k, v in filme.items():
    print(f'O {k} é {v}')
nome = ['Alexandre','Lore', 'Loy', 'chely']
idade = [19, 18, 11, 22]
pessoas = {'nome':nome, 'idade':idade} #lista dentro de dicionarios
print(pessoas.items())
for p in pessoas['nome']:
    print(f'Nome: {p}')

#################Passar um dicionario numa lista###########
p1 = {'Nome': 'Alexandre', 'Idade': 18}
p2 = {'Nome': 'Loyse', 'Idade': 12}
pessoas = list()
pessoas.append(p1)
pessoas.append(p2)
for p in pessoas:
    print('=-'*30)
    print(f'Nome: {p["Nome"]}')
    print(f'Idade: {p["Idade"]}')

############Recebendo varios elementos de um dicionario#############
estado =  dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for est in brasil:
    for i, v in est.items():
        print(f'O campo {i} tem o valor {v}')