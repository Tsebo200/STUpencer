import board
import digitalio
import time
relay = digitalio.DigitalInOut(board.GP16)
from digitalio import DigitalInOut, Direction, Pull #Float Switch

relay = Pin(GP16, Pin.Out)
btn = Pin(GP17, Pin.In)

btn = DigitalInOut(board.SWITCH)
btn.direction = Direction.INPUT
btn.pull = Pull.UP


while True:
    if not btn.value:
        print("BTN is down")
    else:
        print("BTN is up")


time.sleep(0.1) 


# Normal Python code
# while True:
#     logic_state = button.value()
#     if logic_state == True:
#         relay.on()
#     else:
#         relay.off()




    # Add If statement
    # relay.value = True
    # time.sleep(0.5)

    # relay.value = False
    # time.sleep(0.5)





# led.direction = digitalio.Direction.OUTPUT
# led.value = True
# led.value = False

# Button code for Float Switch



