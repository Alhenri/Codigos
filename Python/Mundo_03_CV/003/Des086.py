###Matriz em python####
Matriz = [[],[],[]]
for c1 in range(0, 3):
    for c2 in range(0, 3):
        n = int(input(f'Digite o valor da matriz[{c1}][{c2}]: '))
        Matriz[c1].append(n)
for c1 in Matriz:
    for c2 in c1:
        print(f'[{c2:^5}] ', end='')#:^5 5 casas decimais centralizado
    print()