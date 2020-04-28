pessoas = list()
cadastro = dict()
while True:
    cadastro['Nome'] = str(input("Digite o Nome: "))
    while True:
        cadastro['Sexo'] = str(input("Digite o sexo [M/F]: ")).upper()
        if cadastro['Sexo'] == 'M' or cadastro['Sexo'] == 'F':
            break
        print('Erro, formato inválido!')
    cadastro['Idade'] = int(input("Digite a idade: "))
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while True:
        resp = str(input("Deseja continuar? [S/N]: ")).upper()[0] #pega so a primeira letra
        if resp == 'S' or resp == 'N':
            break
        print('Erro, formato inválido')
    if resp == 'N':
        break

print('=-'*15)
print(f'Você cadastrou {len(pessoas)} pessoas')
media = 0
mulheres = list()

for p in pessoas:
    media += p['Idade']/len(pessoas)
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])

print(f'A média de idades é de {media:5.2f} anos')#5 casas ao todo e 2 decimais
print('=-'*15)
print('>: As mulheres cadastradas são: ')

for p in mulheres:
    print(p)
print('=-'*15)
print('>: Pessoas com idade acima da média são:')
for p in pessoas:
    if p['Idade'] > media:
        print(p['Nome'])