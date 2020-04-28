arquivo = open('texto.text', 'r')#primeiro abre pra ler
texto = arquivo.readlines()#retorna uma lista com todas as linhas
texto.append('65\n')
print(texto)
arquivo.close()
arquivo = open('texto.text', 'w')
arquivo.writelines(texto)
arquivo.close()