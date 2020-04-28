nome = str(input("Digite seu nome: ")).title()
if nome == 'Alexandre':
    print("Nome bonito!")
elif nome in "Ana Pedro João Maria":
    print("Seu nome e bem popular no brasil!")
else:
    print("Nome bem incomum")
print("Tenha um bom dia, {}!".format(nome))