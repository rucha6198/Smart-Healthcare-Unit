#************************************************ Import libraries *************************************************************************
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import csv
import ast
from datetime import datetime
import os

#***************************************** Publish - subscribe initialization *************************************************************
mqttBroker = "192.168.1.108"                 # RPi IP address
SENSOR_TOPIC = "Healthcare_unit"            # topic name for getting sensor values from RPi
PDDL_TOPIC = "Healthcare_unit_pddl"         # topic name for sending actions to RPi

#***************************************** Plan File generation (.txt) ************************************************************************
def parseFile(filename):
    f = open(filename, 'r+')
    lines = f.readlines()[0]
    f.close()

    lines = lines[1:]
    line_split = lines.split()
    action1 = line_split[0]
    print(action1)
    return action1

#**************************************************************** AI Planner defined **********************************************************
def run_planner(domainname, problem, out):
    myCmd = 'python ai_planner_2.py {0} {1} {2}'
    myCmd = myCmd.format(domainname, problem, out)
    os.system(myCmd)
    action = parseFile(out)
    return action

#**************************************************************** CSV file opened*******************************************************************
FILENAME = "IOT_DATA.csv"
header = ['Time', 'Temperature', 'Humidity', 'Pressure', 'Motion', 'Alert', 'Light_int' ]
with open('D:\Courses\Sem 2\Smart cities & IoT\Project\Script\{0}'.format(FILENAME), 'a') as f:

    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)

#************************************************************ Recieve subscribed data via MQTT cloud ***********************************************
def on_message(client, userdata, message):
    s = str(message.payload.decode("utf-8"))
    print("Received message: ", str(message.payload.decode("utf-8")))
    payload_data = ast.literal_eval(s)
    excel_data = {'Time': None, 'Temperature': None, 'Humidity': None, 'Pressure' : None, 'Motion' : None, 'Alert' : None, 'Light_int' : None}
    if 'Motion' in payload_data and payload_data['Motion'] is not None:
        excel_data['Motion'] = payload_data['Motion']
    print(f"Publisher data : {payload_data}")
    print(f"Excel data : {excel_data}")
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    #ts = datetime.timestamp(dt)

#********************************************************* Save recived sensor values into CSV ******************************************************
    f =  open('D:\Courses\Sem 2\Smart cities & IoT\Project\Script\IOT_DATA.csv', 'a', newline='' )
    writer = csv.writer(f, delimiter=',')
    writer.writerow([dt, excel_data, excel_data, excel_data, excel_data['Motion'],excel_data, excel_data])
    f.close()
    #return

    motion_action = None

    domain = 'PIR_Domain.pddl'
    filename = 'pir_plan.txt'
    if excel_data['Motion'] == 1:
        problem = 'PIR_HighProb.pddl'
    else:
        problem = 'PIR_LowProb.pddl'
    motion_action = run_planner(domain, problem, filename)
    print(f"motion_action : {motion_action}")  

    action = {}
    action['motion_action'] = motion_action

#time.sleep(1)

#**************************************** Publisher for sending action to RPi *************************************
    mqtt_payload = str(action)
    print(mqtt_payload)
    publish.single(PDDL_TOPIC, mqtt_payload, hostname = mqttBroker)

# #**************************************** Subscriber for getting sensor data from RPi *************************************
client = mqtt.Client("user")              # Create client object
client.connect(mqttBroker)
client.loop_start()
client.subscribe(SENSOR_TOPIC)
client.on_message = on_message
time.sleep(10000)

#while True:
client.loop_end()



