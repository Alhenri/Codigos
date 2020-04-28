cad = dict()
cad['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
cad['idade'] = 2020 - nascimento
cad['ctps'] = int(input('Digite o numero da CTPS: '))
if cad['ctps'] != 0:
    cad['contratação'] = int(input("Digite o ano de contratação: "))
    cad['salario'] = float(input('Digite o valor do salario: R$ '))
    cad['aposentadoria'] = (cad['contratação']+35)-nascimento
for i, v in cad.items():
    print(f'{i} tem o valor {v}')