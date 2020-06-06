import serial
c = 0
while True:
    porta = f'COM{c}'
    try:
        global arduino
        arduino = serial.Serial(porta, 9600)#porta e baund rate
    except:
        c += 1
    else:
        break


# arduino = serial.Serial(f'COM{c}', 9600)#porta e baund rate

while True:
    msg = str(input('Digite a mensagem que enviará [-1 pra finalizar]: '))
    if msg == '-1':
        break
    arduino.write(msg.encode())
arduino.close()