import serial

arduino = serial.Serial('COM3', 9600)#porta e baund rate

while True:
    msg = str(input('Digite a mensagem que enviará [-1 pra finalizar]: '))
    if msg == '-1':
        break
    arduino.write(msg.encode())