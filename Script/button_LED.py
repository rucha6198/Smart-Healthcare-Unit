from grovepi import*
import time
import math

led_pin= 2
button = 3

pinMode(led_pin, "OUTPUT")
pinMode(button, "INTPUT")

while True:
    try:
        button_state= digitalRead(button)
        print(button_state)
        time.sleep(1)
        if  button_state:
            digitalWrite (led_pin,1)
        else:
            digitalWrite (led_pin,0)
            
    except KeyboardInterrupt:
        digitalWrite (led_pin,0)
        break
    except (IOError, TypeError) as e:
        print("Error")
        