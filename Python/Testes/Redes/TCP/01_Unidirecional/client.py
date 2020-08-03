import socket
HOST = '10.0.0.103'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input('>: ').encode()
while msg != '\x18':
    tcp.send (msg)
    msg = input('>: ').encode()
tcp.close()