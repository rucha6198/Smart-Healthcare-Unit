# csv_writer.py
# Subscriber + csv executed 

#************************************ Import libraries ************************************************
import paho.mqtt.client as mqtt
import time
import ast
import csv
import os


light_sp = 300
temp_sp = 30
pressure_sp = 15
humindity_sp = 100
#************************************* Initialize MQTT parameters **************************************
#mqttBroker = "broker.emqx.io"
#mqttBroker = "mqtt.eclipse.org"
mqttBroker = "mqtt.eclipseprojects.io"
#mqttBroker = "192.168.1.108"
client = mqtt.Client("Hospital")                      #Create an object

#****************************************** Parse file defined *************************************
def parseFile(filename):
    f = open(filename, 'r+')
    test_index = f.readlines()
    
    #print("F.PRINTLINE IS",f.readlines())
    print("F.PRINTLINE IS",test_index,len(test_index))
    
    #lines = f.readlines()[0]
    lines = test_index[0]

    print(lines)
    f.close()

    lines = lines[1:]
    line_split = lines.split()
    action1 = line_split[0]
    print(action1)
    return action1

#*************************************** Excel sheet created *************************************
FILENAME = "IOT_DATA.csv"
header = ['Time', 'Temperature', 'Humidity', 'Pressure', 'Motion', 'Alert', 'Light_int']
with open('D:\Pub_Sub\{0}'.format(FILENAME), 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)

#************************************* Sensor received data from RPi ***********************************
def on_message(client, userdata, message):
    excel_data = {}
    s = str(message.payload.decode("utf-8"))
    print("Received message: ", s)
    #print(s)
    payload_data = eval(s)
    #payload_data = ast.literal_eval(s)
    print(payload_data)
    excel_data = {'Time': None, 'Temperature': None, 'Humidity': None, 'Pressure' : None, 'Motion' : None, 'Alert' : None, 'Light_int' : None}
    
    
    if 'Time' in payload_data and payload_data['Time'] is not None :
        excel_data['Time'] = payload_data['Time']
        
    if 'Temperature' in payload_data and payload_data['Temperature'] is not None:
        excel_data['Temperature'] = payload_data['Temperature']
        

    if 'Humidity' in payload_data and payload_data['Humidity'] is not None:        
        excel_data['Humidity'] = payload_data['Humidity']

    if 'Motion' in payload_data and payload_data['Motion'] is not None:
        excel_data['Motion'] = payload_data['Motion']

    if 'Pressure' in payload_data and payload_data['Pressure'] is not None:
        excel_data['Pressure'] = payload_data['Pressure']

    if 'Alert' in payload_data and payload_data['Alert'] is not None:
        excel_data['Alert'] = payload_data['Alert']
        

    if 'Light_int' in payload_data and payload_data['Light_int'] is not None:
        excel_data['Light_int'] = payload_data['Light_int']
    
    print("Publisher data : , {payload_data}")
    print("Excel data : , {excel_data}")

#************************************* Save sensor values in excel sheet********************************************
    #f = open('D:\Courses\Sem 2\Smart cities & IoT\Project\Script\IOT_DATA.csv', 'a', newline='' )
    f = open('D:\Pub_Sub\IOT_DATA.csv', 'a', newline='')
    writer = csv.writer(f, delimiter=',')
    writer.writerow([ excel_data['Time'],excel_data['Temperature'],excel_data['Humidity'],excel_data['Pressure'],excel_data['Motion'], excel_data['Alert'],  excel_data['Light_int']])
    #writer.writerow([ excel_data['Temperature'],  excel_data['Temperature'],  excel_data['Humidity'],  excel_data['Pressure'], excel_data['Motion'], excel_data['Alert'], excel_data['Light_int']])
    f.close()
    
#*********************************** MQTT Connection*****************************************************************
try:    
    client.connect(mqttBroker)

    #client.loop_start()
    client.subscribe("HEALTH")
    client.on_message = on_message
    #time.sleep()
except Exception as e:
    print(e)


while True:
    try:    
        client.loop_forever()
    except Exception as e:
        print(e)
        continue