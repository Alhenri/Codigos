def notas(*n, sit=False):#significa que recebera varios numeros e guardará num tupla
    """
    by AHSSF
    receber varias notas.......
    recebe se quer ou não ver a situação do aluno
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

#programa principal
resp = notas(4.5, 2.3, 8.5, 1.2, sit=True)
print(resp)
help(notas)