import urequests
import requests
import json
import secrets #imports lib that has ssid and pwd
from machine import PWM, Pin
import time
servo = PWM(Pin(4), freq=50, duty_u16=0)
servoTop = PWM(Pin(5), freq=50, duty_u16=0)


while True:
    
    print("90 Degrees")
    servo.duty_u16(int(0.5*65535/20))
    servoTop.duty_u16(int(0.5*65535/20))
    time.sleep(2)
    print("90 Degrees")
    servo.duty_u16(int(1.53*65535/20))
    servoTop.duty_u16(int(1.5*65535/20))
    time.sleep(2)
    print("180 Degrees")
    servo.duty_u16(int(2.448*65535/20))
    servoTop.duty_u16(int(2.5*65535/20))
    time.sleep(2)


"""
def wifi_connect():
    import network #imports network library to connect to wifi
    
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.SSID, secrets.PWD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))
    
wifi_connect()
token = secrets.at_api_token
lat = 42.3601
lon = -71.0589
DATE_URL = "https://api.api-ninjas.com/v1/worldtime?lat={}&lon={}".format(lat, lon)
headers = {'X-Api-Key': token}
reply = urequests.get(DATE_URL,headers=headers)
response=reply.json()

day=response["day_of_week"]
month=int(response["month"])

if day == "Saturday":
    print("Saturday")
elif day == "Monday":
    print("Monday")
elif day == "Tuesday":
    print("Tuesday")
elif day == "Wednesday":
    print("Wednesday")
elif day == "Thursday":
    print("Thursday")
elif day == "Friday":
    print("Friday")
elif day == "Sunday":
    print("Sunday")
else:
    print("unknown day")

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("unknown month")
"""

