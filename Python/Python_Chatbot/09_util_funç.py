from funcoes import * #importa tudo de outro arquivo de texto
print("-----Bem vindo ao chatboy em python----")
print(">= Olá, qual o seu nome? ")

nome = pegaNome(resposta())
frase = respondeNome(nome)
print(frase+nome)

while True:
    resp = resposta()
    if resp == 'tchau':
        break
    else:
        print('>= Digite outra coisa')
print('>= Tchau!')