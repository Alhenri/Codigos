num = [[],[]]

print('=-'*30)
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n%2 == 0:
        num[0].append(n)
    elif n%2 == 1:
        num[1].append(n)

num[0].sort()#diferente de tuplas, ele faz a transformação real
num[1].sort()
print('=-'*30)
print(f'Pares: {num[0]}')
print(f'Impares: {num[1]}')
print('=-'*30)