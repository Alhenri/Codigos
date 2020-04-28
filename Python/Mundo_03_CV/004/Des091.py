from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
print('Valores sorteado')
print('-='*15)
for j, n in jogo.items():#retorna o indice e o valor do dicionario
    print(f'{j} tirou {n} no dado.')
    sleep(1)
print('-='*15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#Como criei um dicionario, eu preciso passar tanto os 
#indices como os valores (key e values) por isso o método items(). o proximo parametro eu especifico oque desejo ordenar
#de fato 0 para os indices e 1 para os valores. RETORNA TUPLAS DENTRO DE LISTAS
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} no dado.')
    sleep(1)
print('-='*15)