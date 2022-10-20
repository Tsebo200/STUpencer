import time
import board
import digitalio

limitOne = digitalio.DigitalInOut(board.GP15)
limitOne.direction = digitalio.Direction.INPUT
limitOne.pull = digitalio.Pull.UP

limitTwo = digitalio.DigitalInOut(board.GP16)
limitTwo.direction = digitalio.Direction.INPUT
limitTwo.pull = digitalio.Pull.UP

# switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
# switch.direction = digitalio.Direction.INPUT
# switch.pull = digitalio.Pull.UP

while True:
    # print("GP15",limitOne.value)
    # print("GP16",limitTwo.value)

    if limitOne.value:
        print("GP15")
    if limitTwo.value:
        print("GP16")
    # elif switch.value:
    #     print((-1,))
    # else:
    #     print((0,))
    time.sleep(0.1)
