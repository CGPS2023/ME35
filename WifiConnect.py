#importing the libraries
import network
import urequests
import time
import urequests

#setting up SSID and password 
 
SSID = "tufts_eecs" #use tufts_eecs
PASSWORD = "foundedin1883" #foundedin1883


#function definition 
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(0.5)
    print("Connected! IP address:", wlan.ifconfig()[0])
    return wlan
 
 #functiowlan.isconnected()n call
connect_wifi()
 #ON REPL you can type wlan.isconnected() hit ENTER. it will return True
 
ISS_URL = "http://api.open-notify.org/iss-now.json"
response = urequests.get(ISS_URL)
data = response.json()
response.close()
print(data)

#DATE_URL = "https://worldtimeapi.org/api/timezone/America/New_York"
#reply = urequests.get(DATE_URL)
#print(reply.json()['datetime'])


