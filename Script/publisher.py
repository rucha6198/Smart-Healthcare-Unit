# sensor_publisher_3.py code
# Sensor read + Publish sensor data +Subscriber2 + Actuation done

#************************************ Import libraries ************************************************
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

#************************************* Initialize sensor and actuator pins *****************************
light = 0
pir = 1
button = 3
dht11 = 7
pressure = 4

buzzer = 2
led_b = 5
relay = 6
led_r = 8

light_sp = 300
temp_sp = 25
pressure_sp = 500

# Plugwise parameters
DEFAULT_PORT="/dev/ttyUSB0"
mac = "000D6F000567156D"
stick= Stick(DEFAULT_PORT)
circle = Circle(mac,stick)

#************************************* Initialize MQTT parameters **************************************
#mqttBroker = "broker.emqx.io"
#mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "192.168.1.108"              # IP address of Rpi 
client = mqtt.Client("pddl")              #Create object

#**************************************** Functions for sensors *************************************
def pir_motion():                                       # Define function for PIR sensor
    
    payload_data = None
    payload_data = {}
    time.sleep(0.1)
    pir_val = grovepi.digitalRead(pir)
    if pir_val == 255:
        pir_val = 0 
    #print(pir_val)
    payload_data ['Motion'] = int(bool(pir_val))       # PIR sensed value stored in variable
    #print("MOTION IS",payload_data ['Motion'])
    return payload_data

def light_int():
    
    payload_data = None                         # Define function for Light sensor
    payload_data = {}
    time.sleep(1)
    light_val= grovepi.analogRead(light)
    #print(light_val)
    if light_val < 0:
        light_val = 0
    if light_val > 500:
        light_val = 500
    payload_data ['Light_int'] = light_val       # Light intensity value stored in variable
    #print("LIGHT IS",payload_data ['Light_int'])
    #time.sleep(1)
    return payload_data
    

def button_alarm():                             # Define function for button
    payload_data = None
    payload_data = {}
    #time.sleep(0.5)
    button_state= grovepi.digitalRead(button)
    
    if button_state == 1:
        grovepi.digitalWrite(buzzer, 1)
    else: 
        grovepi.digitalWrite(buzzer, 0)
    if button_state == 255:
        button_state = 0 
    payload_data ['Alert'] = int(bool(button_state))       # Button value stored in variable
    #print("BUTTON IS",payload_data ['Alert'])
    #time.sleep(1)
    return payload_data
    

def pressure_sensor():                              # Define function for Pressure Sensor
    payload_data = None
    payload_data = {}
    #time.sleep(1)
    pressure_val = grovepi.ultrasonicRead(pressure)
    if pressure_val > 500:
        pressure_val = 500
    #print(pressure_val)
    payload_data ['Pressure'] = pressure_val       # Pressure sensed value stored in variable
    #print("PRESSURE IS",payload_data ['Pressure'])
    #time.sleep(1)
    return payload_data
    
def temp_hum():                                     # Define function for DHT sensor 
    payload_data = None
    payload_data = {}
    time.sleep(2)
    temp=0
    hum=0
    [temp1,hum1] = grovepi.dht(dht11,0)
    if math.isnan(temp1) or  math.isnan(hum1) or temp1 <0 :
        temp = 24.0
        hum = 43.0 
        print("VALUE IS NAN")
    else:
        temp = temp1
        hum = hum1
        #print(temp)
        #print(hum)

    payload_data ['Temperature'] = temp       # Temperature sensed value stored in variable
    print("TEMP IS",payload_data ['Temperature'])
    #time.sleep(1)

    payload_data ['Humidity'] = hum             # Humidity sensed value stored in variable
    #print("HUM IS",payload_data ['Humidity'])

    return payload_data


#************************************** Sensor data published to Laptop 1 & 2 ******************************
def MQTTDataSend():                             # Data send to MQTT broker 
    print("Data sending started")
    while True:
        payload_data = {}

        ts = time.time()
        x=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        payload_data["Time"] = x

        payload_pir = pir_motion()                              # PIR sensor function called
        if payload_pir is not None:
            if 'Motion' in payload_pir:                       # PIR sensor data stored
                payload_data['Motion'] = payload_pir['Motion']

        
        payload_light = light_int()
        if payload_light is not None:
            if 'Light_int' in payload_light:                       # PIR sensor data stored
                payload_data['Light_int'] = payload_light['Light_int']
 

        payload_button = button_alarm()
        if payload_button is not None:
            if 'Alert' in payload_button:                       # button sensor data stored
                payload_data['Alert'] = payload_button['Alert']

        payload_pressure = pressure_sensor()
        if payload_pressure is not None:
            if 'Pressure' in payload_pressure:                       # presssure sensor data stored
                payload_data['Pressure'] = payload_pressure['Pressure']

        payload_dht = temp_hum()
        if payload_dht is not None:
            if 'Temperature' in payload_dht:
                payload_data['Temperature'] = payload_dht['Temperature']    # Temprature sensor data stored
            if 'Humidity' in payload_dht:
                payload_data['Humidity'] = payload_dht['Humidity']  # Humidity sensor data stored 

#******************************** Publish sensor data *****************************************
        mqtt_payload = str(payload_data)
        client.publish("HEALTH", mqtt_payload)                              #Sensor data Topic = HEALTH
        print("Just published " + mqtt_payload + " to Topic HEALTH")

#********************************* Function for receiving actuation data from Laptop1 ******************************
def on_message(client, userdata, message):                                  # On message received and decoded here
    
    action = str(message.payload.decode("utf-8"))
    print("Received message: ", action)
    payload_pddl = eval(action)
    #payload_pddl = ast.literal_eval(action)

#**************************************** Actuation Funtions *********************************************
    #motion_output = None
    light_output = None
    temp_output = None
    #button_output = None
    pressure_output =None
    hum_output = None
    
    '''if 'motion_action' in payload_pddl and payload_pddl['motion_action'] is not None:
        motion_output = payload_pddl['motion_action']'''

    
    if 'light_action' in payload_pddl and payload_pddl['light_action'] is not None:     #Saving Light output action 
        light_output = payload_pddl['light_action']

    if 'temp_action' in payload_pddl and payload_pddl['temp_action'] is not None:       #Saving temprature action
        temp_output = payload_pddl['temp_action']

    '''if 'button_action' in payload_pddl and payload_pddl['button_action'] is not None:
        button_output = payload_pddl['button_action']'''

    if 'pressure_action' in payload_pddl and payload_pddl['pressure_action'] is not None:   #Saving Pressure action
        pressure_output = payload_pddl['pressure_action']

    if 'hum_action' in payload_pddl and payload_pddl['hum_action'] is not None:         #Saving Humidity action
        hum_output = payload_pddl['hum_action']
    
    #motion_actuation(motion_output)
    light_actuation(light_output)
    temp_actuation(temp_output)
    pressure_actuation(pressure_output)
    #button_actuation(button_output)
    humidity_actuation(hum_output)

'''def motion_actuation(motion_output):

    if motion_output == 'switchonlight':
        print("LED ON")
        #grovepi.digitalWrite (led_r,1)
    else:
        print("LED OFF")
        #grovepi.digitalWrite (led_r,0)'''



def light_actuation(light_output):                          # Turn on Blue LED if switchonled is received from the planner
    pir_value = grovepi.digitalRead(pir)
    if (light_output == 'switchonled') :
        print("Blue LED ON")
        grovepi.digitalWrite (led_b,1)
    else:
        print("Blue LED OFF")
        grovepi.digitalWrite (led_b,0)

def temp_actuation(temp_output):                            # Turn on heater if switchonheater is received from the planner
    # Plugwise
    if temp_output == 'switchonheater':
        print("Heater ON")
        circle.switch_on()
    else:
        print("Heater OFF")
        circle.switch_off()

def pressure_actuation(pressure_output):                    # Turn on LED if switchon_led is received from the planner
    if pressure_output == 'switchon_led':
        print("LED ON")
        grovepi.digitalWrite (led_r,1)
    else:
        print("LED OFF")
        grovepi.digitalWrite (led_r,0)

'''def button_actuation(button_output):
    if button_output == 'switchon_buzzer':
        print("Buzzer ON")
        grovepi.digitalWrite(buzzer,1)
    #   time.sleep(0.1)
    else:
        print("Buzzer OFF")
        grovepi.digitalWrite(buzzer,0)'''

def humidity_actuation(hum_output):                         # Turn on Relay if switchonhumidifier is received from the plann
    if hum_output == 'switchonhumidifier':
        print("Relay ON")
        grovepi.digitalWrite (relay,1)
    else:
        print("Relay OFF")
        grovepi.digitalWrite (relay,0)


def pddlMQTTDataReceive():
    print("Connected to broker")    
    client.subscribe("HEALTH_PDDL")             # PDDL topic = HEALTH_PDDL
    client.loop_forever()

#**************************************** MQTT parameters ***********************************
client.connect(mqttBroker)                                  # Connect to mqtt broker


client.on_message = on_message                              # trigger On message if any message comes

t1 = threading.Thread(target=MQTTDataSend)                  # Threading task 1
t2 = threading.Thread(target=pddlMQTTDataReceive)           # Threading task 2
t1.start()
t2.start()








