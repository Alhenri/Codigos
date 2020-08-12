# É melhor fazer uma comunicação bidirecional com dois termienais em paralelo
#ele serão unidos por um 3 arquivo que irá executar os dois ao mesmo tempo

import socket

# Configuração da comunicação
print("-= Configuração do chat -=")
ip_loc = input(str('Digite o IP local: '))
ip_dest = input(str('Digite o IP destino: '))
port = input(str('Digite a porta: '))

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #objeto TCP
origin = (ip_loc, port)
dest = (ip_dest, port)

# configurando recepção
tcp.bind(origin)
tcp.listen(1)

def comHost(HostOk):

    # To ouvindo o client
    con, client = HostOk()
    print(f'-=-= {client} já está ouvindo-=-=')

    while True:
        try:
            # tenta falar
            tcp.connect(dest)
            biCom(con)
        except:
            pass

def comClient():
    pass

def biCom(Host):
    pass

while True:
    try:
        tcp.connect(dest)
    except:
        comHost(tcp.accept)