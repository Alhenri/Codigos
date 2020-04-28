pessoa1 = {'Nome':'Alexandre','Idade':19}
pessoa2 = {'Nome':'José', 'Idade':22}
lista = list()
lista.append(pessoa1)
lista.append(pessoa2)

for p in lista:
    print(p['Nome'])