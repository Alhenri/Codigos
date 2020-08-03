import socket
HOST = '10.0.0.103'              # Endereco IP do Servidor
PORT = 3000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criando o udp
orig = (HOST, PORT) # definindo a origen da conexão
udp.bind(orig) # Criando o servidor
while True:
    msg, cliente = udp.recvfrom(1024) # Capturando mensage,
    msg.decode()
    print (f'{cliente}: {msg}')
udp.close() #fechando server