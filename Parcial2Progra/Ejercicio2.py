import pyfirmata
from pyfirmata import Arduino
import time

port = "\\.\COM4" #Puerto COM de emulación en USB
pauseTime = 0.3

#Conexión con placa Arduino
print("Conectando con Arduino por USB...")
tarjeta = Arduino(port)
print("Conectado a Arduino por USB.")

def turnLedsON(a,b,sleep):
    for contLeds in range(a,b):
        tarjeta.digital[contLeds].write(1)
    time.sleep(sleep)

def turnLedsOFF(a,b):
    for contLeds in range(a,b):
        tarjeta.digital[contLeds].write(0)
    time.sleep(pauseTime)

#Ciclo While ejecutado al infinito
while True:
    turnLedsON(2,7,1)
    turnLedsOFF(2,7)

    turnLedsON(6,11,2)
    turnLedsOFF(6,11)
tarjeta.exit()