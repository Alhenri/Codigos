import socket
HOST = '10.0.0.103'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print (f'Concetado por {cliente}')
    while True:
        msg = con.recv(1024).decode()
        if not msg: break
        print(f'{cliente}: {msg}')
    print (f'Finalizando conexao do cliente {cliente}')
    con.close()