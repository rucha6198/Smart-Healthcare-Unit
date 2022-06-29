#************************************************ Import libraries **************************************************************
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscibe
import time
import grovepi
from grovepi import*

#**************************************** Publish - subscribe initialization ***************************************************
#mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "192.168.1.108"                 # RPi IP address
SENSOR_TOPIC = "Healthcare_unit"            # topic name for sending sensor values to RPi
PDDL_TOPIC = "Healthcare_unit_pddl"         # topic name for getting actions From RPi

#************************************* Initialization of sensor pins ********************************************************
button = 5

client = mqtt.Client("PDDL")                  # Create client object
client.connect(mqttBroker)

while True:
    button_state = grovepi.digitalRead(button)
    client.publish("Healthcare_unit", button_state)
    print("Just published " + str(button_state) + " to Healthcare_unit")
    time.sleep(1)

    

