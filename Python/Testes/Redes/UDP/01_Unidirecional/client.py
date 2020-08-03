import socket
HOST = '10.0.0.103'  # Endereco IP do Servidor
PORT = 3000          # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X')
msg = input("Mensagem: ").encode()
while msg != '\x18':
    udp.sendto (msg, dest)
    msg = input("Mensagem: ").encode()
udp.close()