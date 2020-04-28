lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite o numero da posição {c}: ')))
pos_Maior = list()
pos_Menor = list()
maior_n = 0
for n in lista:
    if n > maior_n:
        maior_n = n
menor_n = maior_n
for n in lista:
    if n < menor_n:
        menor_n = n
for p, n in enumerate(lista):
    if n == maior_n:
        pos_Maior.append(p)
for p,  n in enumerate(lista):
    if n == menor_n:
        pos_Menor.append(p)
print(f'O maior numero foi {maior_n} e estava na posição: ', end='')
for n in pos_Maior:
    print(f'{n} ', end='')
print()
print(f'O menor numero foi {menor_n} e estava na posição: ', end='')
for n in pos_Menor:
    print(f'{n} ', end='')

##################Curso em video###########
#ele pegou os maiores e menores assim:
#for c in range(0, 5):
#    listanum.append(input())
#    if c == 0:
#        mai = men = listanum[c]
#    else:
#        if listanum[c] > mai:
#            mai = listanum[c]
#        if listanum[c] < men:
#            men = listanum[c]