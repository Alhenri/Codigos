aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a media do aluno: '))
print(f'Aluno: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
if aluno['media']>= 7:
    print('Aporvado!')
elif 5 <= aluno['media'] < 7:
    print('Recuperação!')
else:
    print('Reprovado!')