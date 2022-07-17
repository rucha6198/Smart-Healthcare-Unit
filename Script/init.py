import grovepi
from grovepi import*
from plugwise.api import*
from grove_rgb_lcd import *
import time

light = 0
pir = 1
button = 3
dht = 7
pressure = 4

buzzer = 2
led_b = 5
relay = 6
led_r = 8

DEFAULT_PORT="/dev/ttyUSB0"
mac = "000D6F000567156D"
stick= Stick(DEFAULT_PORT)
circle = Circle(mac,stick)

grovepi.digitalWrite (led_r,0)
grovepi.digitalWrite (led_b,0)
grovepi.digitalWrite (buzzer,1)
time.sleep(2)
grovepi.digitalWrite (buzzer,0)
grovepi.digitalWrite (relay,0)
circle.switch_off()


setRGB(0,128,64)

setRGB(0,255,0)
setText("                               ")


