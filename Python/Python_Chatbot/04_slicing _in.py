#É pegar partes de uma estring
print("-----Bem vindo ao chatboy em python----")
print(">= Olá, qual o seu nome? ")
nome = str(input(">= ")).title()
if 'Meu Nome É' in nome:
    n = nome.find('Meu Nome É')+11
    nome = nome[n:]
if nome == 'Alexandre':
    print(f"Eaew {nome}")
else:
    print(f"Muito prazer {nome}")
