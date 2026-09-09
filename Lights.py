import neopixel #importing the library
import random
from machine import Pin # another way of importing a library
import time
lights = neopixel.NeoPixel(Pin(15),2) # 0 is the Pin for neopixel and 4 is the number of lights
lights[0] = (20,0,20) # set the color of 0th light to purple 
lights.write()
i=0
while i <= 100:
    for j in range(100):
    lights[0] = (i, j, i+100)
    lights.write()
    time.sleep_ms(25)
i=i+1

