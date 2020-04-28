times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
        'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')

print('=-'*30)
print(f'Os 5 primeiros colocados {times[:5]}')
print('=-'*30)
print(f'Os 4 ultimos colocados {times[16:]}')
print('=-'*30)
print(f'Lista em ordem alfabetica:')

t_ordem = sorted(times)
for v, c in enumerate(t_ordem):
    print(f'{v+1}º - {c}')
print('=-'*30)
print(f'A Chapecoense está em {times.index("Chapecoense")+1}º')