import pyfirmata
from pyfirmata import Arduino
import time

port = "\\.\COM4" #Puerto COM de emulación en USB
pauseTime = 0.2

#Conexión con placa Arduino
print("Conectando con Arduino por USB...")
board = Arduino(port)
print("Conectado a Arduino por USB.")

def ledsCascada(a,b,c):
     #Ciclo for para encender en cascada
    for contLeds in range(a,b,c):
        board.digital[contLeds].write(1)
        time.sleep(pauseTime)
        board.digital[contLeds].write(0)

#Ciclo While ejecutado al infinito
while True:
   ledsCascada(2,11,1)
   ledsCascada(10,1,-1)
    
tarjeta.exit()