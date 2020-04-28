vel = float(input("Qual a velocidade do carro? "))
if vel > 80:
    multa = (vel-80)*7
    print("Você foi multado no valor de R$ {:.2f}".format(multa))
else:
    print("Tá suave, po passar!")