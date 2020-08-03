import os
from datetime import datetime

# print(f'Diretório atual: {os.getcwd()}')
# os.chdir('/Users/Usuario/Desktop')

print('=-'*20)
print(f'Diretório atual: {os.getcwd()}')


os.makedirs('teste/olá') # cria um caminho
os.removedirs('teste/olá') # remove todo o caminho


# mod_time = os.stat('texto.txt').st_mtime # Mostra o timestamp da data de modificação
# mod_time = datetime.fromtimestamp(mod_time)

# print ( f"Data de modificação do arquivo: {mod_time}")

print(os.listdir())
print('=-'*20)

# juntando dois diretorios da forma correta
print(os.environ.get('HOME')) # pega variaveis de ambiente
file_path = os.path.join(os.environ.get('HOME'), 'teste129.txt')

print('=-'*20)
# Modificando diretorios
print(f'Nome do diretório: {os.path.dirname(os.getcwd())}')
print(f'Nome da base: {os.path.basename(os.getcwd())}')
print(f'Split: {os.path.split(os.getcwd())}')
print(f'Existencia: {os.path.exists(os.getcwd())}') # isdir, isfile, splitext
