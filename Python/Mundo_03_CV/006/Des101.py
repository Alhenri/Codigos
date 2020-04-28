def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 65 > idade >= 18:
        return f'Com {idade}: o voto é OBRIGATÓRIO'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade}: o voto é OPCIONAL'
    else:
        return f'Com {idade}: o voto é PROIBIDO'

print(voto(int(input('Ano de nascimento: '))))        