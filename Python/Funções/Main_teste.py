import my_doc


arquivo = 'cursoemvideo.txt'
perg = int(input('[1] Adiciona pessoa\n[2] Ler arquivo\nResposta: '))

if perg == 1:
    while True:
        pessoa = list()
        pessoa.append(input('Nome: '))
        pessoa.append(input('Idade: '))
        pessoa.append(input('Sexo: '))
        my_doc.escreve_txt(arquivo, pessoa)
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp == 'N':
            break

elif perg == 2:
    n = int(input('Quantas keys o dicionário terá? (dados por linha): '))
    keys = list()
    for c in range(0, n):
        keys.append(str(input(f'Key {c+1}: ')))

    pessoas = my_doc.ler_txt(arquivo, keys)
    print(pessoas)