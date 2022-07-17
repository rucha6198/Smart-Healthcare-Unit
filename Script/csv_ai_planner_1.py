# csv_ai_planner_1.py
# Subscriber1 + Excel + Plan generation +Publish2   executed 

#************************************ Import libraries ************************************************
import paho.mqtt.client as mqtt
import time
import ast
import csv
import os


light_sp = 300
temp_sp = 30
pressure_sp = 25
humindity_sp = 40
#************************************* Initialize MQTT parameters **************************************
#mqttBroker = "broker.emqx.io"

#mqttBroker = "mqtt.eclipse.org"
#mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "192.168.1.108"
client = mqtt.Client("Smartphone")                      #Create an object

#****************************************** Parse file defined *************************************
def parseFile(filename):                            # extracting plan from the generated plan
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

#*************************************** AI planner file ******************************************
def run_planner(domainname, problem, out):          # Run planner API is called
    myCmd = 'python ai_planner_2.py {0} {1} {2}'
    myCmd = myCmd.format(domainname, problem, out)
    os.system(myCmd)
    action = parseFile(out)
    return action

#*************************************** Excel sheet created *************************************
'''FILENAME = "IOT_DATA.csv"
header = ['Time', 'Temperature', 'Humidity', 'Pressure', 'Motion', 'Alert', 'Light_int']
with open('E:\Software Workspaces\iot_group12\Copy\Script_app1\{0}'.format(FILENAME), 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)'''

#************************************* Sensor received data from RPi ***********************************
def on_message(client, userdata, message):
    excel_data = {}
    s = str(message.payload.decode("utf-8"))
    print("Received message: ", s)
    #print(s)
    payload_data = eval(s)
    #payload_data = ast.literal_eval(s)
    print(payload_data)                     # Payload is saved to excel sheet
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
    '''f = open('E:\Software Workspaces\iot_group12\Copy\Script_app1\IOT_DATA.csv', 'a', newline='')
    writer = csv.writer(f, delimiter=',')
    writer.writerow([ excel_data['Time'],excel_data['Temperature'],excel_data['Humidity'],excel_data['Pressure'],excel_data['Motion'], excel_data['Alert'],  excel_data['Light_int']])
    #writer.writerow([ excel_data['Temperature'],  excel_data['Temperature'],  excel_data['Humidity'],  excel_data['Pressure'], excel_data['Motion'], excel_data['Alert'], excel_data['Light_int']])
    f.close()'''
    
#******************************************* PDDL files *****************************************888888
    #motion_action = None
    light_action = None
    pressure_action = None
    #button_action = None
    temp_action = None
    hum_action = None

# PIR PDDL
    '''domain = 'PIR_Domain.pddl' 
    filename = 'PIR_plan.txt'
    print(excel_data['Motion'])
    if excel_data['Motion'] == 1:
        problem = 'PIR_HighProb.pddl'
        print("ON plan created")
    else:
        problem = 'PIR_LowProb.pddl'
        print("OFF plan created")
    motion_action = run_planner(domain, problem, filename)
    print(f"motion_action : {motion_action}")'''

# Light_intensity PDDL
    domain = 'Light_intensity_Domain.pddl'          #Light PDDL is called 
    filename = 'light_plan.txt'
    print(excel_data['Light_int'])
    if excel_data['Light_int'] < light_sp :
        problem = 'Light_intensity_HighProb.pddl'
        print("ON plan created")
    else:
        problem = 'Light_intensity_LowProb.pddl'
        print("OFF plan created")
    light_action = run_planner(domain, problem, filename)

# Pressure PDDL
    domain = 'Pressure_Domain.pddl'                 # Pressure PDDL is called 
    filename = 'pressure_plan.txt'
    print(excel_data['Pressure'])
    if excel_data['Pressure'] < pressure_sp:
        problem = 'Pressure_HighProb.pddl'
        print("ON plan created")
    else:
        problem = 'Pressure_LowProb.pddl'
        print("OFF plan created")
    pressure_action = run_planner(domain, problem, filename)

# Button PDDL
    '''domain = 'Button_Domain.pddl' 
    filename = 'button_plan.txt'
    print(excel_data['Alert'])
    if excel_data['Alert'] == 1:
        problem = 'Button_HighProb.pddl'
        print("ON plan created")
    else:
        problem = 'Button_LowProb.pddl'
        print("OFF plan created")
    button_action = run_planner(domain, problem, filename)'''


# Temperature PDDL                                  # Temprature PDDL is called
    domain = 'Temp_Domain.pddl' 
    filename = 'temp_plan.txt'
    print(excel_data['Temperature'])
    if excel_data['Temperature'] > temp_sp :
        problem = 'Temp_HighProb.pddl'
        print("ON plan created")
    else:
        problem = 'Temp_LowProb.pddl'
        print("OFF plan created")
    temp_action = run_planner(domain, problem, filename)
  
# Humidity PDDL                                     # Humidity PDDL is called 
    domain = 'Hum_Domain.pddl' 
    filename = 'hum_plan.txt'
    print(excel_data['Humidity'])
    if excel_data['Humidity'] > humindity_sp:
        problem = 'Hum_HighProb.pddl'
        print("OFF plan created")
    else:
        problem = 'Hum_LowProb.pddl'
        print("ON plan created")
    hum_action = run_planner(domain, problem, filename)


    action = {}
    #action['motion_action'] = motion_action
    #print("Action[motion]", action['motion_action'])
    action['light_action'] = light_action
    action['pressure_action'] = pressure_action
    #action['button_action'] = button_action
    action['temp_action'] = temp_action
    action['hum_action'] = hum_action
    

#************************************** Publish actuation data to RPi *******************************            
    mqtt_payload = str(action)                      # Payload data is created
    print(mqtt_payload)
    client.publish("HEALTH_PDDL", mqtt_payload)     # payload is published
    print("Just published " + mqtt_payload + " to Topic HEALTH_PDDL")

    return

#**************************************** MQTT parameters to receive data *****************************
'''#while True:
client.connect(mqttBroker)

#client.loop_start()
client.subscribe("HEALTH")
client.on_message = on_message
#time.sleep(4)'''

try:    
    client.connect(mqttBroker)              # Client is connected

    #client.loop_start()
    client.subscribe("HEALTH")              # Topic is created
    client.on_message = on_message          # On message function is triggered
    #time.sleep(4)
except Exception as e:
    print(e)                                   # try and except for error handling


while True:
    try:    
        client.loop_forever()                   # Continious connection with client for sendig actions
    except Exception as e:
        print(e)
        continue