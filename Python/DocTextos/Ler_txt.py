arquivo = open('texto.text', 'r')
texto = arquivo.readlines()#retorna uma lista com todas as linhas
print(texto)
arquivo.close()