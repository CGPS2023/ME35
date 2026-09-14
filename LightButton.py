import neopixel #importing the library
import random
from machine import Pin # another way of importing a library
import time
from time import ticks_ms, ticks_diff
#In is detecting current, out is supplying current
btn=Pin(34,Pin.IN,Pin.PULL_UP)
lights = neopixel.NeoPixel(Pin(15),2) # 0 is the Pin for neopixel and 4 is the number of lights
DEBOUNCE_MS = 200
last_press = 0
on=0;
lights[0] = (13,40,140) # set the color of 0th light to purple 
lights.write()
def button_handler(pin):
    global last_press
    now = ticks_ms()
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        if (pin.value() == 0):
            last_press = now
            on=1
            print("Button pressed!")
            print(on)
        else:
            on=0
while true:
    btn.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
    if on==1:
        lights[0] = (20,0,20) # set the color of 0th light to purple 
        lights.write()
    elif on==0:
        lights[0] = (13,40,140) # set the color of 0th light to purple 
        lights.write()
    


