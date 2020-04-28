numeros = list()
n_par = list()
n_impar = list()
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    if n%2 == 0:
        n_par.append(n)
    elif n%2 == 1:
        n_impar.append(n)
    resp  = str(input('Deseja adicionar mais numeros? [S/N]: ')).lower()
    if resp == 'n':
        break
print(f'Numeros digitados: {numeros}')
print(f'Numeros pares: {n_par}')
print(f'Numeros impares: {n_impar}')