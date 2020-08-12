import socket

HOST = '10.0.0.101'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

print("Conectando...")
while True:
    try:
        tcp.connect(dest)
        break
    except:
        pass


print('-=-= Voce se está conectado -=-=')
print('-=-= Digite -* para sair -=-=')

while True:
    msg = input('>: ').encode() #transformando a string em bytes
    print('-='*15)  
    flag = msg.decode() #pegando um flag para verificação
    
    try:
        tcp.send (msg) #enviando mensagem
    except:
        print("Server: Host se desconectou!")
        print("Server: Digite -* para cancelar a comunicação")
 
    
    if flag == '-*':
        tcp.close()
        break #comparando o flag