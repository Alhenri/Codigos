def leiInt(perg):
    while True:
        n = str(input(perg))
        if n.isnumeric():
            return int(n)
        else:
            print('Erro! Digite um inteiro válido')

n = leiInt('Digite um numero: ')
print(f'Você digitou o numero {n}')