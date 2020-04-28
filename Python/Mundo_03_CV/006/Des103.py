def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')
n = str(input('Nome do jogador: '))
g = str(input('Gols marcados: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)