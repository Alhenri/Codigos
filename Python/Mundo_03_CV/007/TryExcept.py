try:#tenta fazer algo, um mesmo try pode ter varios except
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
#except Exception as erro:#se houver erro
#    print(f'Problema foi encontrado em: {erro.__class__}')#pega a classe que o invocou
except (ValueError, TypeError):
    print('Tipo de dado não suportado')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
else:#se nao houver erro
    print(f'O resultado é {r:.1f}')
finally:#idependente do erro
    print('Volte sempre!')