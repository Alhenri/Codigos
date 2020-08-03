arquivo = open('Testes/texto.txt', 'r')
msg = arquivo.read()

print()
print('-='*5+'Bem vindo a cifra de fluxo'+'-='*5)
cript = int(input(">: chave: "))
msg_cript = ''
for c in range(len(msg)):
    msg_cript += chr(ord(msg[c])^cript)
print('-'*10)
print(f'>: Resultado\n{msg_cript}')
arquivo.close()

print('-'*10)
op = int(input('Deseja salva a encriptação? digite 1: '))
print('-'*10)

if(op == 1):
    newArquivo = open('Testes/texto.txt', 'w')
    newArquivo.write(msg_cript)
    print('Texto encriptado!')
    print('-'*10)