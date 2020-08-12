import socket
HOST = '10.0.0.101'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept() # Recebe o objeto do cliente, e o endereço do cliente
    print(f'-=-= Concetado por {cliente} -=-=')
    print('-=-= Digite -* para sair -=-=')
    print('-='*15)

    while True:
        msg = con.recv(1024).decode() # 1024 é o tamanho do buffer
        if msg == '-*': break
        print(f'{cliente}: {msg}')
        print('-='*15)

    print (f'-=-= Finalizando conexao do cliente {cliente} -=-=')
    con.close()
