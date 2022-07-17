from grovepi import *
import time
from grove_rgb_lcd import *
import math

dht_sensor_port = 7

while True:
    try:

        [temp,hum] = dht(dht_sensor_port,0) 
        if math.isnan(temp) or  math.isnan(hum) or temp <0 :
            setText("Temp:    C      Humidty :     %     ")
        else:
            temp1 = temp
            hum1 = hum

        print ("temp =", temp1, "C\thumidity =", hum1, "%")
        time.sleep(1)
        t= str(temp1)
        h = str(hum1)

        setRGB(0,128,64)

        setRGB(0,255,0)
        setText("Temp:" + t + "C   " + "   Humidty :" + h + "%")

    except (IOError, TypeError) as e:
        print ("Error")
