import pyfirmata
from pyfirmata import Arduino
import time

board = pyfirmata.Arduino('COM4')

pauseTime = 1

#Checkear el status de los leds, si esta encendido imprime 'ON' de lo contrario imprime 'OFF'
def checkStatus():
    statusLed = board.digital[contLeds].read()
    if statusLed == 1:
        statusLed = 'ON'
    if statusLed == 0:
        statusLed = "OFF"
    print("Status Led#",contLeds,"-->",statusLed)

while True:
    #Ciclo for para encender en ascendente
    for contLeds in range(2,11):
        board.digital[contLeds].write(1)
        checkStatus()
        time.sleep(pauseTime)
        board.digital[contLeds].write(0)
        checkStatus()

    #Ciclo for para enceder en descente
    for contLeds in range(10, 1, -1):
        board.digital[contLeds].write(1)
        checkStatus()
        time.sleep(pauseTime)
        board.digital[contLeds].write(0)
        checkStatus()
tarjeta.exit()