import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

limitOne = digitalio.DigitalInOut(board.GP15)
limitOne.direction = digitalio.Direction.INPUT
limitOne.pull = digitalio.Pull.UP

limitTwo = digitalio.DigitalInOut(board.GP14)
limitTwo.direction = digitalio.Direction.INPUT
limitTwo.pull = digitalio.Pull.UP

relay = DigitalInOut(board.GP17)
relay.direction = Direction.OUTPUT

# switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
# switch.direction = digitalio.Direction.INPUT
# switch.pull = digitalio.Pull.UP

while True:
    # print("GP15",limitOne.value)
    # print("GP16",limitTwo.value)
    if limitOne.value:
        relay.value = True
        print("GP15")

    else:
        relay.value = False

    if limitTwo.value:
        print("Yes")
        # relay.value = False
    else:
        print("No Tsebo")
    time.sleep(0.1)
    #     relay.value = False

    # elif switch.value:
    #     print((-1,))
    # else:
    #     print((0,))
    # time.sleep(0.1)

