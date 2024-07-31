import Stepper
import machine
from machine import Pin
import time
import machine, neopixel
import os

interval = 12 # interval (How long the microcontroler will wait until next feed in hours)
#interval = 0.01 # test (36 seconds)
ColorToggle = True

# Create a NeoPixel object and light it up green
np = neopixel.NeoPixel(machine.Pin(16), 1)
np[0] = (0, 64, 0)
np.write()

# Create a Stepper object
s1 = Stepper.create(Pin(9,Pin.OUT),Pin(10,Pin.OUT),Pin(11,Pin.OUT),Pin(12,Pin.OUT), delay=5,mode='HALF_STEP')

while True:
    # Step to the next cell
    s1.step(-17)
    
    # Waits interval the toggle the color (between red and blue) to indicate the fish was fed
    time.sleep_ms(int(interval*60*60*1000))
    ColorToggle = not ColorToggle
    if ColorToggle:
        np[0] = (0, 0, 64)
    else:
        np[0] = (64, 0, 0)
    np.write()
