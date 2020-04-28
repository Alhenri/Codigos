def escreva(txt):
    print('-'*(len(txt)+2))
    print(f' {txt} ')
    print('-'*(len(txt)+2))

while True:
    escreva(str(input('Digite o texto: ')))