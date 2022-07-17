from numpy import dtype
import paho.mqtt.client as mqtt
import time
import grovepi
from grovepi import*
import threading
import ast
from datetime import datetime
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import math
from plugwise.api import*
from grove_rgb_lcd import *


light = 0
pir = 1
button = 3
dht11 = 7
pressure = 4

buzzer = 2
led_b = 5
relay = 6
led_r = 8

light_val= grovepi.analogRead(light)

if light_val < 0:
    light_val = 0
    print(light_val)
if light_val > 500:
    light_val = 500
    print(light_val)
print(light_val)

pir_value = grovepi.digitalRead(pir)

if (light_val<300) and (pir_value == 1):
    print("Blue LED ON")
    grovepi.digitalWrite (led_b,1)
else:
    print("Blue LED OFF")
    grovepi.digitalWrite (led_b,0)
