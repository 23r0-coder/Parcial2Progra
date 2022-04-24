import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
pauseTime = 1.3

def ledsCascadaPot(a,b,c):
     #Ciclo for para encender en cascada
    for contLeds in range(a,b,c):
        analog_value = analog_input.read()
        if analog_value is not None:
            pausePot = pauseTime - analog_value
            board.digital[contLeds].write(1)
            time.sleep(pausePot)
            board.digital[contLeds].write(0)

#Ciclo While ejecutado al infinito
while True:
    ledsCascadaPot(2,11,1)
    ledsCascadaPot(10,1,-1)
tarjeta.exit()