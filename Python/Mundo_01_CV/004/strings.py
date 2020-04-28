frase = "Curso em video python"
#fatiamento de string
print("frase inteira: "+frase)
print("intervalo 4 a 6: "+frase[3:7])
print("intervalo do 5 ate o final de 2 em 2: "+frase[5::2])
#analise de string
print("tamanho: {}".format(len(frase)))
print("Quantidade de 'e': {}".format(frase.count("o")))
print("Quantidade de 'o' de 7 ate o fim: {}".format(frase.count("o", 7)))
print("Que momento da cadeia começou 'deo': {}".format(frase.find('deo')))
print("Existe a palavra 'Curso' na frase? {}".format('Curso' in frase))
#Transformação de string
print(frase.replace('python','Android'))#Substituição
print(frase.upper())#tudo maisculo
print(frase.lower())#tudo minusculo
print(frase.capitalize())#tudo minusculo menos a primeira letra
print(frase.title())#capitalize po palavra
print(frase.strip())#remove os espaços vazios dos lados da string lstrip ou rstrip
#Divisão de string
dividido = frase.split()#gera uma lista com as palavras (array)
print(dividido)
print(dividido[2][3])
#Junção
print('-'.join(dividido))