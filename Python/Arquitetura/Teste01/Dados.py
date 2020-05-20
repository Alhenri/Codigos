def retornaDados():
    print('    Buscando dados no banco de dados...')
    import criaDados as cd
    dado = cd.Pessoa('Alexandre', 'Soares', 19)
    print('    retornando dados para a chamada...')
    return dado
def salvaDados():
    print('    Recebendo dados da interface...')
    print('    Salvando dados em arquivo JSON...')