import digitalio
import board
import time

##N = 0
##F = N +1 

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:

    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
    ##if F == 1000:
   ## break