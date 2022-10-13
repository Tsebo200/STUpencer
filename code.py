from multiprocessing.sharedctypes import Value
import board
import digitalio
import time
relay = digitalio.DigitalInOut(board.GP16)

from digitalio import DigitalInOut, Direction, Pull #Float Switch

btn = DigitalInOut(board.SWITCH)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:

    # Add If statement
    relay.value = True
    time.sleep(0.5)

    relay.value = False
    time.sleep(0.5)



    



# led.direction = digitalio.Direction.OUTPUT
# led.value = True
# led.value = False

# Button code for Float Switch



