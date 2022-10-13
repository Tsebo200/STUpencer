import board
import digitalio
led = digitalio.DigitalInOut(board.GP16)
import time

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

# led.direction = digitalio.Direction.OUTPUT
# led.value = True
# led.value = False