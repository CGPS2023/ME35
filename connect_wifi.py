#importing the libraries
import network
import urequests
import time
import urequests
import Secrets
 
#setting up SSID and password 
#Why isn't it working?
SSID = Secrets.SSID
PASSWORD = Secrets.PASSWORD


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