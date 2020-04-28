##########Uma tupla que pode ser mudado os valores################
lista = ['cha', 'cafe', 'coca', 'suco']
lista.append('açai')#adiciona um item a lista
lista.insert(0,'batata')#adiciona um item a uma posição especifica
del lista[1] #apaga o que tiver a posição 0 e realoca o resto
lista.pop(1)#idem mas se passada sem parametros elimina o ultimo item
lista.remove('coca')#remove algo pelo conteudo e realoca o resto, se não existir gera erro
valores = list(range(4,11))#cria uma lista com valores de 4 a 11 ordenada
valores = [8,2,3,5,3,1,5,2]#lista desordenada
valores.sort()#ordena a lista de forma crescente
valores.sort(reverse=True)#ordena a lista de forma decrescente
len(valores)#numero de elementos
b = []
a = b #cria uma ligação entre as listas
a = b[:]#cria uma copia sem ligação das listas
teste = []
for cont in range(0, 5):
    teste.append(input('Digite um valor: '))

for c, v in enumerate(teste):
    print(f'Na posição {c} encontrei o valor {v}')
print('fim da lista')