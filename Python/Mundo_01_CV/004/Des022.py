frase = input("Digite seu nome completo: ")
print("Seu nome todo maiusculo: "+frase.upper())
print("Seu nome com todas as letras minusculas: "+frase.lower())
print("Quantidade de letras é {}".format(len(frase)-frase.count(' ')))
divi = frase.split()
print("Quatidade de letras do primeiro nome é {}".format(len(divi[0])))